#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Pure Python finger protocol implementation.

finger is both a protocol and a utility to get the information and
status from a user on a distant machine. It was standardized in RFC 742
in 1977, then in RFC 1288 in 1991, and has been abandoned by most
people since.

This Python module is a finger server implementation that allows you
to give out real information as well as fictional information.

For more information, consult the documentation at `pyfingerd.org`_.

.. _pyfingerd.org: https://pyfingerd.org/
"""

from __future__ import annotations


__version__ = "0.5.1"
