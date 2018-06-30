import pytest

import logging

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ister.log as log

def setup_logging(level, file):
    name = 'foo.bar'
    log.setup_logging(level, file, name=name)
    return logging.getLogger(name)


def test_setup_info(tmpdir):
    logger = setup_logging('info', os.path.join(tmpdir, 'xxxxxx'))
    assert len(logger.handlers) == 2
    assert os.path.basename(logger.handlers[1].stream.name) == 'xxxxxx'
    assert logger.handlers[0].level == logging.INFO


def test_setup_debug(tmpdir):
    logger = setup_logging('debug', os.path.join(tmpdir, 'zzzz'))
    assert len(logger.handlers) == 2
    assert os.path.basename(logger.handlers[1].stream.name) == 'zzzz'
    assert logger.handlers[0].level == logging.DEBUG


def test_setup_error(tmpdir):
    logger = setup_logging('error', os.path.join(tmpdir, 'log'))
    assert logger.handlers[0].level == logging.ERROR
