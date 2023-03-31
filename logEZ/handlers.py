import logging

def get_console_handler(formatter):
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    return consoleHandler


def get_file_handler(log_file_name, formatter):
    fileHandler = logging.FileHandler(log_file_name)
    fileHandler.setFormatter(formatter)
    return fileHandler
