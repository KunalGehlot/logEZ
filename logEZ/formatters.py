import logging

def get_default_formatter():
    return logging.Formatter(
        "%(asctime)s - %(name)s : %(levelname)s : %(message)s", "%d-%m-%y %H:%M:%S"
    )
