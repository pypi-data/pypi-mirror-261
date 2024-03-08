#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Main script of the module."""

from __future__ import annotations

from .cli import cli as _cli


if __name__ == "__main__":
    _cli()
