import os
import logging
import pytest
from context import logEZ  # noqa: F401
from logEZ.mylogger import MyLogger, root_logger


def test_mylogger_init_defaults():
    """
    Test MyLogger initialization with default parameters.
    """
    logger = MyLogger()
    assert logger.logging_levels["INFO"] == logging.INFO
    assert os.path.exists("logEZ.log")


def test_mylogger_init_custom_parameters():
    """
    Test MyLogger initialization with custom parameters.
    """
    logger = MyLogger(
        log_file_name="custom.log",
        logging_level="DEBUG",
        disable_console_logs=True,
        disable_file_logs=False,
    )
    assert logger.logging_levels["DEBUG"] == logging.DEBUG
    assert os.path.exists("custom.log")


def test_mylogger_set_logging_level():
    """
    Test changing the logging level of MyLogger.
    """
    logger = MyLogger()
    logger.set_logging_level("WARNING")
    assert root_logger.level == logging.WARNING


@pytest.mark.parametrize(
    "level,expected", [("DEBUG", logging.DEBUG), ("ERROR", logging.ERROR)]
)
def test_mylogger_set_logging_level_parametrized(level, expected):
    """
    Test changing the logging level of MyLogger with parametrized inputs.
    """
    logger = MyLogger()
    logger.set_logging_level(level)
    assert root_logger.level == expected


def test_mylogger_disable_both_logs_exception():
    """
    Test MyLogger initialization raising an exception
    when both console and file logs are disabled.
    """
    with pytest.raises(
        Exception, match="Both console and file logs are disabled"
    ):
        MyLogger(disable_console_logs=True, disable_file_logs=True)
