import logging
from .handlers import get_console_handler, get_file_handler
from .formatters import get_default_formatter

rootLogger = logging.getLogger()


class MyLogger:
    def __init__(
        self,
        log_file_name="logEZ.log",
        logging_level="INFO",
        disable_console_logs=False,
        disable_file_logs=False,
    ) -> None:

        if disable_console_logs and disable_file_logs:
            raise Exception("Both console and file logs are disabled")

        self.logging_levels = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        logFormatter = get_default_formatter()

        rootLogger.setLevel(self.logging_levels[logging_level])

        if not disable_file_logs:
            fileHandler = get_file_handler(log_file_name, logFormatter)
            rootLogger.addHandler(fileHandler)

        if not disable_console_logs:
            consoleHandler = get_console_handler(logFormatter)
            rootLogger.addHandler(consoleHandler)

        self.myDebug("logEZ initialized...")

    # Other logging methods...
