# Copyright Modal Labs 2022
import asyncio
import contextlib
import dataclasses
import os
from multiprocessing.synchronize import Event
from typing import TYPE_CHECKING, AsyncGenerator, List, Optional, TypeVar

from rich.console import Console

from modal_proto import api_pb2
from modal_utils.app_utils import is_valid_app_name
from modal_utils.async_utils import TaskContext, synchronize_api
from modal_utils.grpc_utils import retry_transient_errors

from ._container_exec import container_exec
from ._output import OutputManager, get_app_logs_loop, step_completed, step_progress
from .app import _LocalApp, is_local
from .client import HEARTBEAT_INTERVAL, HEARTBEAT_TIMEOUT, _Client
from .config import config
from .exception import InteractiveTimeoutError, InvalidError, _CliUserExecutionError

if TYPE_CHECKING:
    from .stub import _Stub
else:
    _Stub = TypeVar("_Stub")


async def _heartbeat(client, app_id):
    request = api_pb2.AppHeartbeatRequest(app_id=app_id)
    # TODO(erikbern): we should capture exceptions here
    # * if request fails: destroy the client
    # * if server says the app is gone: print a helpful warning about detaching
    await retry_transient_errors(client.stub.AppHeartbeat, request, attempt_timeout=HEARTBEAT_TIMEOUT)


@contextlib.asynccontextmanager
async def _run_stub(
    stub: _Stub,
    client: Optional[_Client] = None,
    stdout=None,
    show_progress: bool = True,
    detach: bool = False,
    output_mgr: Optional[OutputManager] = None,
    environment_name: Optional[str] = None,
    shell=False,
    interactive=False,
) -> AsyncGenerator[_Stub, None]:
    """mdmd:hidden"""
    if environment_name is None:
        environment_name = config.get("environment")

    if not is_local():
        raise InvalidError(
            "Can not run an app from within a container."
            " Are you calling stub.run() directly?"
            " Consider using the `modal run` shell command."
        )
    if stub._local_app:
        raise InvalidError(
            "App is already running and can't be started again.\n"
            "You should not use `stub.run` or `run_stub` within a Modal `local_entrypoint`"
        )

    if stub.description is None:
        import __main__

        if "__file__" in dir(__main__):
            stub.set_description(os.path.basename(__main__.__file__))
        else:
            # Interactive mode does not have __file__.
            # https://docs.python.org/3/library/__main__.html#import-main
            stub.set_description(__main__.__name__)

    if client is None:
        client = await _Client.from_env()
    if output_mgr is None:
        output_mgr = OutputManager(stdout, show_progress, "Running app...")
    if shell:
        output_mgr._visible_progress = False
    app_state = api_pb2.APP_STATE_DETACHED if detach else api_pb2.APP_STATE_EPHEMERAL
    app = await _LocalApp._init_new(
        client,
        stub.description,
        environment_name=environment_name,
        app_state=app_state,
        interactive=interactive,
    )
    async with stub._set_local_app(app), TaskContext(grace=config["logs_timeout"]) as tc:
        # Start heartbeats loop to keep the client alive
        tc.infinite_loop(lambda: _heartbeat(client, app.app_id), sleep=HEARTBEAT_INTERVAL)

        with output_mgr.ctx_if_visible(output_mgr.make_live(step_progress("Initializing..."))):
            initialized_msg = f"Initialized. [grey70]View run at [underline]{app.log_url()}[/underline][/grey70]"
            output_mgr.print_if_visible(step_completed(initialized_msg))
            output_mgr.update_app_page_url(app.log_url())

        # Start logs loop
        if not shell:
            logs_loop = tc.create_task(get_app_logs_loop(app.app_id, client, output_mgr))

        exc_info: Optional[BaseException] = None
        try:
            # Create all members
            await app._create_all_objects(stub._indexed_objects, app_state, environment_name, output_mgr=output_mgr)

            # Update all functions client-side to have the output mgr
            for obj in stub.registered_functions.values():
                obj._set_output_mgr(output_mgr)

            # Update all the classes client-side to propagate output manager to their methods.
            for obj in stub.registered_classes.values():
                obj._set_output_mgr(output_mgr)

            # Show logs from dynamically created images.
            # TODO: better way to do this
            output_mgr.enable_image_logs()

            # Yield to context
            if shell:
                yield stub
            else:
                with output_mgr.show_status_spinner():
                    yield stub
        except KeyboardInterrupt as e:
            exc_info = e
            # mute cancellation errors on all function handles to prevent exception spam
            for obj in stub.registered_functions.values():
                obj._set_mute_cancellation(True)

            if detach:
                output_mgr.print_if_visible(step_completed("Shutting down Modal client."))
                output_mgr.print_if_visible(
                    f"""The detached app keeps running. You can track its progress at: [magenta]{app.log_url()}[/magenta]"""
                )
                if not shell:
                    logs_loop.cancel()
            else:
                output_mgr.print_if_visible(
                    step_completed(f"App aborted. [grey70]View run at [underline]{app.log_url()}[/underline][/grey70]")
                )
                output_mgr.print_if_visible(
                    "Disconnecting from Modal - This will terminate your Modal app in a few seconds.\n"
                )
        except BaseException as e:
            exc_info = e
            raise e
        finally:
            if isinstance(exc_info, KeyboardInterrupt):
                reason = api_pb2.APP_DISCONNECT_REASON_KEYBOARD_INTERRUPT
            elif exc_info is not None:
                reason = api_pb2.APP_DISCONNECT_REASON_LOCAL_EXCEPTION
            else:
                reason = api_pb2.APP_DISCONNECT_REASON_ENTRYPOINT_COMPLETED

            if isinstance(exc_info, _CliUserExecutionError):
                exc_str = repr(exc_info.__cause__)
            elif exc_info:
                exc_str = repr(exc_info)
            else:
                exc_str = ""

            await app.disconnect(reason, exc_str)
            stub._uncreate_all_objects()

    output_mgr.print_if_visible(
        step_completed(f"App completed. [grey70]View run at [underline]{app.log_url()}[/underline][/grey70]")
    )


async def _serve_update(
    stub,
    existing_app_id: str,
    is_ready: Event,
    environment_name: str,
) -> None:
    """mdmd:hidden"""
    # Used by child process to reinitialize a served app
    client = await _Client.from_env()
    try:
        app = await _LocalApp._init_existing(client, existing_app_id)

        # Create objects
        output_mgr = OutputManager(None, True)
        await app._create_all_objects(
            stub._indexed_objects, api_pb2.APP_STATE_UNSPECIFIED, environment_name, output_mgr=output_mgr
        )

        # Communicate to the parent process
        is_ready.set()
    except asyncio.exceptions.CancelledError:
        # Stopped by parent process
        pass


@dataclasses.dataclass(frozen=True)
class DeployResult:
    """Dataclass representing the result of deploying an app."""

    app_id: str


async def _deploy_stub(
    stub: _Stub,
    name: str = None,
    namespace=api_pb2.DEPLOYMENT_NAMESPACE_WORKSPACE,
    client=None,
    stdout=None,
    show_progress=True,
    environment_name: Optional[str] = None,
    public: bool = False,
) -> DeployResult:
    """Deploy an app and export its objects persistently.

    Typically, using the command-line tool `modal deploy <module or script>`
    should be used, instead of this method.

    **Usage:**

    ```python
    if __name__ == "__main__":
        deploy_stub(stub)
    ```

    Deployment has two primary purposes:

    * Persists all of the objects in the app, allowing them to live past the
      current app run. For schedules this enables headless "cron"-like
      functionality where scheduled functions continue to be invoked after
      the client has disconnected.
    * Allows for certain kinds of these objects, _deployment objects_, to be
      referred to and used by other apps.
    """
    if environment_name is None:
        environment_name = config.get("environment")

    if name is None:
        name = stub.name
    if name is None:
        raise InvalidError(
            "You need to either supply an explicit deployment name to the deploy command, or have a name set on the app.\n"
            "\n"
            "Examples:\n"
            'stub.deploy("some_name")\n\n'
            "or\n"
            'stub = Stub("some-name")'
        )

    if not is_valid_app_name(name):
        raise InvalidError(
            f"Invalid app name {name}. App names may only contain alphanumeric characters, dashes, periods, and underscores, and must be less than 64 characters in length. "
        )

    if client is None:
        client = await _Client.from_env()

    output_mgr = OutputManager(stdout, show_progress)

    app = await _LocalApp._init_from_name(client, name, namespace, environment_name=environment_name)

    async with TaskContext(0) as tc:
        # Start heartbeats loop to keep the client alive
        tc.infinite_loop(lambda: _heartbeat(client, app.app_id), sleep=HEARTBEAT_INTERVAL)

        # Don't change the app state - deploy state is set by AppDeploy
        post_init_state = api_pb2.APP_STATE_UNSPECIFIED

        try:
            # Create all members
            await app._create_all_objects(
                stub._indexed_objects, post_init_state, environment_name=environment_name, output_mgr=output_mgr
            )

            # Deploy app
            # TODO(erikbern): not needed if the app already existed
            url = await app.deploy(name, namespace, public)
        except Exception as e:
            # Note that AppClientDisconnect only stops the app if it's still initializing, and is a no-op otherwise.
            await app.disconnect(reason=api_pb2.APP_DISCONNECT_REASON_DEPLOYMENT_EXCEPTION)
            raise e

    output_mgr.print_if_visible(step_completed("App deployed! 🎉"))
    output_mgr.print_if_visible(f"\nView Deployment: [magenta]{url}[/magenta]")
    return DeployResult(app_id=app.app_id)


async def _interactive_shell(_stub: _Stub, cmd: List[str], environment_name: str = "", **kwargs):
    """Run an interactive shell (like `bash`) within the image for this app.

    This is useful for online debugging and interactive exploration of the
    contents of this image. If `cmd` is optionally provided, it will be run
    instead of the default shell inside this image.

    **Example**

    ```python
    import modal

    stub = modal.Stub(image=modal.Image.debian_slim().apt_install("vim"))
    ```

    You can now run this using

    ```bash
    modal shell script.py --cmd /bin/bash
    ```

    **kwargs will be passed into spawn_sandbox().
    """
    client = await _Client.from_env()
    async with _run_stub(_stub, client, environment_name=environment_name, shell=True):
        console = Console()
        loading_status = console.status("Starting container...")
        loading_status.start()

        sb = await _stub.spawn_sandbox("sleep", "360000", **kwargs)

        for _ in range(40):
            await asyncio.sleep(0.5)
            resp = await sb._client.stub.SandboxGetTaskId(api_pb2.SandboxGetTaskIdRequest(sandbox_id=sb._object_id))
            if resp.task_id != "":
                task_id = resp.task_id
                break
            # else: sandbox hasn't been assigned a task yet
        else:
            loading_status.stop()
            raise InteractiveTimeoutError("Timed out while waiting for sandbox to start")

        loading_status.stop()
        await container_exec(task_id, cmd, pty=True, client=client, terminate_container_on_exit=True)


run_stub = synchronize_api(_run_stub)
serve_update = synchronize_api(_serve_update)
deploy_stub = synchronize_api(_deploy_stub)
interactive_shell = synchronize_api(_interactive_shell)
