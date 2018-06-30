#!/usr/bin/env python3
"""Linux installation template system"""

#
# This file is part of ister.
#
# Copyright (C) 2014 Intel Corporation
#
# ister is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 3 of the License, or (at your
# option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

# We aren't using classes for anything other than with handling so
# a warning about too few methods being implemented isn't useful.
# pylint: disable=too-few-public-methods
# We aren't worried too much about performance of ister itself here, so using
# .format() for the logging functions (which always formats the string) is ok.
# pylint: disable=logging-format-interpolation

import logging
import sys


logging.getLogger().setLevel(logging.DEBUG)


def setup_logging(level, logfile, *, name=None, shandler=logging.StreamHandler(sys.stdout)):
    """Setup log levels and direct logs to a file"""

    log = logging.getLogger(name)
    log.handlers = []

    shandler.setLevel(logging.INFO)
    if level == 'debug':
        shandler.setLevel(logging.DEBUG)
    elif level == 'error':
        shandler.setLevel(logging.ERROR)
    log.addHandler(shandler)

    if logfile:
        open(logfile, 'w').close()
        fhandler = logging.FileHandler(logfile)
        fhandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s-%(levelname)s: %(message)s')
        fhandler.setFormatter(formatter)
        log.addHandler(fhandler)


def debug(*args, name=None, **kwargs):
    logging.getLogger(name).debug(*args, **kwargs)


def info(*args, name=None, **kwargs):
    logging.getLogger(name).info(*args, **kwargs)


def error(*args, name=None, **kwargs):
    logging.getLogger(name).error(*args, **kwargs)

