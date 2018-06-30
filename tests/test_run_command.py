import pytest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ister.run_command import run_command


def test_run_command_good():
    run_command('true')


def test_run_command_no_binary():
    run_command('not-a-binary', False)


def test_run_command_no_binary_exception():
    with pytest.raises(Exception):
        run_command('not-a-binary')
