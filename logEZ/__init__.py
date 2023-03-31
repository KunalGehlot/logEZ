from .mylogger import MyLogger


def create_logger(*args, **kwargs):
    return MyLogger(*args, **kwargs)
