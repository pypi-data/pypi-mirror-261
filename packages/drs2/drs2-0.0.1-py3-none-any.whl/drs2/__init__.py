import logging
from logging.handlers import TimedRotatingFileHandler
import os
import socket
from datetime import datetime

__version__ = "0.0.1"

LOG_FILE_BACKUP_COUNT = os.getenv('LOG_FILE_BACKUP_COUNT')
LOG_ROTATION = "midnight"

container_id = socket.gethostname()
timestamp = datetime.today().strftime('%Y-%m-%d')


def configure_logger():  # pragma: no cover
    log_level = os.getenv("APP_LOG_LEVEL", "WARNING")
    log_file_path = os.getenv("LOGFILE_PATH",
                              "/app/logs/drs2_judaica_update")
    formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - ' +
                '[%(filename)s:%(funcName)s:%(lineno)d] - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger('drs2_judaica_update')
    logger.addHandler(console_handler)
    # Defaults to console logging
    if ((os.getenv("CONSOLE_LOGGING_ONLY", "true")).strip()) == "false":
        file_handler = TimedRotatingFileHandler(
            filename=f"{log_file_path}/{container_id}_console_{timestamp}.log",
            when=LOG_ROTATION,
            backupCount=LOG_FILE_BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(log_level)
