import logging
from parking_system.utility.constants import LOGGER_NAME, DEFAULT_LOG_LEVEL
import os

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger(LOGGER_NAME)
log_level = (
    os.environ.get("LOG_LEVEL") if os.environ.get("LOG_LEVEL") else DEFAULT_LOG_LEVEL
)

if log_level == "DEBUG":
    logger.setLevel(logging.DEBUG)
elif log_level == "WARNING":
    logger.setLevel(logging.WARNING)
else:
    logger.setLevel(logging.INFO)
