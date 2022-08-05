import logging

logFormatter = logging.Formatter(
    '%(asctime)s - %(name)s : %(levelname)s : %(message)s',
    '%d-%m-%y %H:%M:%S'
    # Use structure: 17-11-21 11:26:34 - root : DEBUG : MyLogger initialized...
)

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

# Save logs to smartReader.log file
fileHandler = logging.FileHandler('smartReader.log')
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

# Show logs on console also
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


class MyLogger:
    def __init__(self) -> None:
        self.myDebug('MyLogger initialized...')

    def setLoggingLevel(self, level):
        rootLogger.setLevel(level)

    def myDebug(self, inString):
        rootLogger.debug(inString)

    def myInfo(self, inString):
        rootLogger.info(inString)

    def myWarn(self, inString):
        rootLogger.warning(inString)

    def myError(self, inString, exc_info=False):
        rootLogger.error(inString, exc_info=exc_info)

    def myCrit(self, inString, exc_info=False):
        rootLogger.critical(inString, exc_info=exc_info)

    def myExecpt(self, inString):
        rootLogger.exception(inString)
