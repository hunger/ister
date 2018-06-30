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

# If we see an exception it is always fatal so the broad exception
# warning isn't helpful.
# pylint: disable=broad-except
# We aren't using classes for anything other than with handling so
# a warning about too few methods being implemented isn't useful.
# pylint: disable=too-few-public-methods
# We aren't worried too much about performance of ister itself here, so using
# .format() for the logging functions (which always formats the string) is ok.
# pylint: disable=logging-format-interpolation


import shlex
import subprocess
import sys

from .log import (debug, info, error)

def run_command(cmd, raise_exception=True, log_output=True, environ=None,
                show_output=False, shell=False):
    """Execute given command in a subprocess

    This function will raise an Exception if the command fails unless
    raise_exception is False.
    """
    try:
        debug("Running command {0}".format(cmd))
        sys.stdout.flush()
        if shell:
            full_cmd = cmd
        else:
            full_cmd = shlex.split(cmd)
        proc = subprocess.Popen(full_cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                env=environ,
                                shell=shell)

        def process_output(output, *, show_output=False, log_output=False):
            result = []
            for line in output:
                decoded_line = line.decode('ascii', 'ignore').rstrip()
                if show_output:
                    info(decoded_line)
                elif log_output:
                    debug(decoded_line)
                result.append(decoded_line)
            return result

        stdout = process_output(proc.stdout, show_output=show_output, log_output=log_output)
        stderr = process_output(proc.stderr, show_output=show_output, )

        if proc.poll() and raise_exception:
            if stderr:
                debug("Error {0}".format('\n'.join(stderr)))
            raise Exception(cmd)
        return stdout, proc.returncode
    except Exception as exep:
        if raise_exception:
            raise Exception("{0} failed: {1}".format(cmd, exep))
