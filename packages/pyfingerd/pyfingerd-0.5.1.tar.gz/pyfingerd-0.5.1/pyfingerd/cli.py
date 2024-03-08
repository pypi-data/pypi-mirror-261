#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2021-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""pyfingerd CLI interface."""

from __future__ import annotations

from datetime import datetime as _datetime
from os import (
    EX_IOERR as _EX_IOERR,
    EX_OSFILE as _EX_OSFILE,
    EX_USAGE as _EX_USAGE,
)
from platform import (
    python_implementation as _python_impl,
    python_version as _python_version,
)
from sys import exit as _sys_exit

import click as _click
import coloredlogs as _coloredlogs

from . import __version__ as _version
from .core import FingerInterface as _FingerInterface
from .errors import BindError as _BindError
from .fiction import (
    FingerScenario as _FingerScenario,
    FingerScenarioInterface as _FingerScenarioInterface,
)
from .native import FingerNativeInterface as _FingerNativeInterface
from .server import FingerServer as _FingerServer
from .utils import logger as _logger


__all__ = ["cli"]


@_click.command(context_settings={"help_option_names": ["-h", "--help"]})
@_click.version_option(
    version=_version,
    message=(
        f"pyfingerd version {_version}, "
        + f"running on {_python_impl()} {_python_version()}"
    ),
)
@_click.option(
    "-b",
    "--binds",
    default="localhost:79",
    envvar=("BIND", "BINDS"),
    show_default=True,
    help="Addresses and ports on which to listen to, comma-separated.",
)
@_click.option(
    "-H",
    "--hostname",
    default="LOCALHOST",
    envvar=("FINGER_HOST",),
    show_default=True,
    help="Hostname to display to finger clients.",
)
@_click.option(
    "-t",
    "--type",
    "type_",
    default=None,
    envvar=("FINGER_TYPE",),
    show_default=True,
    help="Interface type for gathering user and session data.",
)
@_click.option(
    "-s",
    "--scenario",
    default=None,
    envvar=("FINGER_SCENARIO", "FINGER_ACTIONS"),
    help="Path to the scenario, if the selected type is 'scenario'.",
)
@_click.option(
    "-S",
    "--start",
    "scenario_start",
    type=_click.DateTime(),
    default=_datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    envvar=("FINGER_START",),
    help=(
        "Date and time at which the scenario starts or has started "
        + "as an ISO date, if the selected type is 'scenario'."
    ),
)
@_click.option(
    "-l",
    "--loglevel",
    "log_level",
    default="info",
    envvar=("FINGER_LOGLEVEL",),
    help="Log level for the displayed messages.",
)
def cli(
    binds: str,
    hostname: str,
    type_: str,
    scenario: str | None,
    scenario_start: _datetime,
    log_level: str,
) -> None:
    """Start a finger (RFC 1288) server.

    Find out more at <https://pyfingerd.org/>.
    """
    _coloredlogs.install(
        fmt="\r%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        level=log_level.upper(),
    )

    hostname = hostname.upper()

    if type_ is None:
        if scenario is not None:
            type_ = "scenario"
        else:
            type_ = "native"

    type_ = type_.casefold()
    if scenario is not None and type_ not in ("actions", "scenario"):
        _logger.warning(
            "Since the type isn't 'scenario', the provided scenario "
            + "path will be ignored.",
        )

    if type_ == "native":
        iface = _FingerNativeInterface()
    elif type_ in ("actions", "scenario"):
        if scenario is None:
            _logger.error(
                "Scenario interface selected, but the scenario has not "
                + "been provided; please do so.",
            )
            _sys_exit(_EX_USAGE)

        try:
            fic = _FingerScenario.load(scenario)
            iface = _FingerScenarioInterface(fic, scenario_start)
        except (FileNotFoundError, PermissionError):
            _logger.error("Error opening the scenario:", exc_info=True)
            _sys_exit(_EX_OSFILE)
        except ValueError as exc:
            message = str(exc)
            _logger.error("Error loading the scenario:")
            _logger.error("%s%s.", message[0].upper(), message[1:])
            _sys_exit(_EX_OSFILE)
    else:
        if type_ != "dummy":
            _logger.warning(
                "Unknown interface type %r, falling back on dummy",
                type_,
            )

        iface = _FingerInterface()

    try:
        server = _FingerServer(binds, hostname=hostname, interface=iface)
    except _BindError as exc:
        _logger.error("%s", exc.original_message)
        _sys_exit(_EX_IOERR)

    server.serve_forever()
