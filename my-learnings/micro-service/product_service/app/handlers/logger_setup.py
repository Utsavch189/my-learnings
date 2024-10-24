import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

def get_currentTime():
    return datetime.now().strftime("%d-%m-%Y")

def get_filename()->str:
    return f"logs/{get_currentTime()}.log"

class TimeAndSizeRotatingHandler(RotatingFileHandler):

    def __init__(self, filename: str=get_filename(), mode: str = "a", maxBytes: int = 0, backupCount: int = 0, encoding: str | None = None, delay: bool = False, errors: str | None = None) -> None:
        self.baseFilename=filename
        self.maxBytes=maxBytes
        self._lastUpdateTime=get_currentTime()
        super().__init__(get_filename(), mode, maxBytes, backupCount, encoding, delay, errors)
    
    def shouldRollover(self, record: logging.LogRecord) -> int:
        """
        When the rollover will happen, this method decides.
        return True means new rollover.
        """
        if(get_currentTime()!=self._lastUpdateTime):
            # Time period is checked here
            self.baseFilename=get_filename()
            self._lastUpdateTime=get_currentTime()
            return True
        return super().shouldRollover(record)

    def emit(self, record):
        """
        Emit a record.

        Overrides RotatingFileHandler.emit to include custom behavior before
        calling the parent class's emit method.
        """

        # Call the parent class's emit method to write to file
        super().emit(record)

    def doRollover(self):
        """
        Do a rollover.

        Overrides RotatingFileHandler.doRollover to add custom behavior after
        the rollover is done.

        When max size while emitting is reached doRollover is called!
        """
        # Perform the rollover using the parent class's method
        super().doRollover()

logger = logging.getLogger()

handler = TimeAndSizeRotatingHandler(
    maxBytes=5*1024*1024, backupCount=9999
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)