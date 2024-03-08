#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2021-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd Python 3.x module, which is MIT-licensed.
# *****************************************************************************
"""Utilities for the pyfingerd module."""

from __future__ import annotations

from datetime import timedelta as _timedelta
import logging as _logging
import re as _re
from typing import ClassVar as _ClassVar


__all__ = [
    "UnchangedType",
    "Unchanged",
    "access_logger",
    "error_logger",
    "format_delta",
    "logger",
    "parse_delta",
]

__delta0_re = _re.compile(r"(-?)(([0-9]+[a-z]+)+)")
__delta1_re = _re.compile(r"([0-9]+)([a-z]+)")

logger = _logging.getLogger("pyfingerd")
access_logger = _logging.getLogger("pyfingerd.access")
error_logger = _logging.getLogger("pyfingerd.error")


class UnchangedType:
    """Special constant class for representing 'no changes required'."""

    __slots__ = ()

    __unchanged_value__: _ClassVar[UnchangedType]

    def __new__(cls: type[UnchangedType], *args, **kwargs):
        """Construct the class."""
        # We want the same instance to be returned always when required.
        try:
            return cls.__unchanged_value__
        except AttributeError:
            value = super().__new__(cls, *args, **kwargs)
            cls.__unchanged_value__ = value
            return value

    def __repr__(self):
        return "Unchanged"


Unchanged = UnchangedType()


def parse_delta(raw: str) -> _timedelta | None:
    """Parse a delta string as found in the configuration files."""
    delta = _timedelta()

    match = __delta0_re.fullmatch(raw)
    if match is None:
        return None

    sign, elements, _ = match.groups()
    sign = (1, -1)[len(sign)]
    for res in __delta1_re.finditer(elements):
        num, typ = res.groups()
        num = int(num)

        if typ == "w":
            delta += _timedelta(weeks=sign * num)
        elif typ in "jd":
            delta += _timedelta(days=sign * num)
        elif typ == "h":
            delta += _timedelta(hours=sign * num)
        elif typ == "m":
            delta += _timedelta(minutes=sign * num)
        elif typ == "s":
            delta += _timedelta(seconds=sign * num)
        else:
            return None

    return delta


def format_delta(delta: _timedelta, /) -> str:
    """Create a delta string."""
    sls = zip(
        (
            _timedelta(days=7),
            _timedelta(days=1),
            _timedelta(seconds=3600),
            _timedelta(seconds=60),
        ),
        "wdhm",
    )

    if delta >= _timedelta():
        d = ""

        for span, letter in sls:
            n = delta // span
            if n:
                d += f"{n}{letter}"
                delta -= span * n

        s = delta.seconds
        if not d or s:
            d += f"{s}s"
    else:
        d = "-"

        for span, letter in sls:
            n = -delta // span
            if n:
                d += f"{n}{letter}"
                delta += span * n

        s = (-delta).seconds
        if s:
            d += f"{s}s"

    return d


def make_delta(value: str | int | float | _timedelta | None) -> _timedelta:
    """Make a delta from a raw value."""
    if value is None:
        raise ValueError("must not be None")

    if isinstance(value, _timedelta):
        return value

    try:
        value = int(value)
    except (TypeError, ValueError) as exc:
        if isinstance(value, str):
            new_value = parse_delta(value)
            if new_value is not None:
                return new_value

            raise ValueError(f"invalid time delta: {value!r}") from exc

        raise TypeError(f"unknown type {type(value).__name__}") from exc

    return _timedelta(seconds=value)
