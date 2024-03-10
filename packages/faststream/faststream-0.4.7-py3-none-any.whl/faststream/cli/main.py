import logging
import sys
import warnings
from contextlib import suppress
from typing import Dict, List, Optional

import anyio
import typer
from click.exceptions import MissingParameter
from pydantic import ValidationError
from typer.core import TyperOption

from faststream.__about__ import INSTALL_WATCHFILES, __version__
from faststream.cli.docs.app import docs_app
from faststream.cli.utils.imports import import_from_string
from faststream.cli.utils.logs import LogLevels, get_log_level, set_log_level
from faststream.cli.utils.parser import parse_cli_args
from faststream.types import SettingField

cli = typer.Typer(pretty_exceptions_short=True)
cli.add_typer(docs_app, name="docs", help="AsyncAPI schema commands")


def version_callback(version: bool) -> None:
    """Callback function for displaying version information.

    Args:
        version: If True, display version information

    Returns:
        None
    """
    if version is True:
        import platform

        typer.echo(
            "Running FastStream {} with {} {} on {}".format(
                __version__,
                platform.python_implementation(),
                platform.python_version(),
                platform.system(),
            )
        )

        raise typer.Exit()


@cli.callback()
def main(
    version: Optional[bool] = typer.Option(
        False,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show current platform, python and FastStream version",
    ),
) -> None:
    """Generate, run and manage FastStream apps to greater development experience."""


@cli.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def run(
    ctx: typer.Context,
    app: str = typer.Argument(
        ...,
        help="[python_module:FastStream] - path to your application",
    ),
    workers: int = typer.Option(
        1,
        show_default=False,
        help="Run [workers] applications with process spawning",
    ),
    log_level: LogLevels = typer.Option(
        LogLevels.info,
        case_sensitive=False,
        show_default=False,
        help="[INFO] default",
    ),
    reload: bool = typer.Option(
        False,
        "--reload",
        is_flag=True,
        help="Restart app at directory files changes",
    ),
    watch_extensions: List[str] = typer.Option(
        (),
        "--extension",
        "--reload-extension",
        "--reload-ext",
        "--ext",
        help="List of file extensions to watch by",
    ),
    app_dir: str = typer.Option(
        ".",
        "--app-dir",
        help=(
            "Look for APP in the specified directory, by adding this to the PYTHONPATH."
            " Defaults to the current working directory."
        ),
    ),
) -> None:
    """Run [MODULE:APP] FastStream application."""
    if watch_extensions and not reload:
        typer.echo(
            "Extra reload extensions has no effect without `--reload` flag."
            "\nProbably, you forgot it?"
        )

    app, extra = parse_cli_args(app, *ctx.args)
    casted_log_level = get_log_level(log_level)

    if app_dir:  # pragma: no branch
        sys.path.insert(0, app_dir)

    args = (app, extra, casted_log_level)

    if reload and workers > 1:
        raise ValueError("You can't use reload option with multiprocessing")

    if reload is True:
        try:
            from faststream.cli.supervisors.watchfiles import WatchReloader
        except ImportError:
            warnings.warn(INSTALL_WATCHFILES, category=ImportWarning, stacklevel=1)
            _run(*args)

        else:
            module_path, _ = import_from_string(app)

            WatchReloader(
                target=_run,
                args=args,
                reload_dirs=[str(module_path)] + ([app_dir] if app_dir else []),
            ).run()

    elif workers > 1:
        from faststream.cli.supervisors.multiprocess import Multiprocess

        Multiprocess(
            target=_run,
            args=(*args, logging.DEBUG),
            workers=workers,
        ).run()

    else:
        _run(*args)


def _run(
    # NOTE: we should pass `str` due FastStream is not picklable
    app: str,
    extra_options: Dict[str, SettingField],
    log_level: int = logging.INFO,
    app_level: int = logging.INFO,
) -> None:
    """Runs the specified application.

    Args:
        app: path to FastStream application.
        extra_options: Additional options for the application.
        log_level: Log level for the application (default: logging.INFO).
        app_level: Log level for the application (default: logging.INFO).

    Returns:
        None

    Note:
        This function uses the `anyio.run()` function to run the application.
    """
    _, app_obj = import_from_string(app)

    set_log_level(log_level, app_obj)

    if sys.platform not in ("win32", "cygwin", "cli"):  # pragma: no cover
        with suppress(ImportError):
            import uvloop

            uvloop.install()  # type: ignore[attr-defined]

    try:
        anyio.run(
            app_obj.run,
            app_level,
            extra_options,
        )

    except ValidationError as e:
        ex = MissingParameter(
            param=TyperOption(param_decls=[f"--{x['loc'][0]}" for x in e.errors()])
        )

        try:
            from typer import rich_utils

            rich_utils.rich_format_error(ex)
        except ImportError:
            ex.show()

        sys.exit(1)
