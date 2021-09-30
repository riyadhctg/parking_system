from enum import Enum


DEFAULT_DB_CONNECTION_STRING = ":memory:"
LOGGER_NAME = "parking_system_logger"
DEFAULT_LOG_LEVEL = "DEBUG"


# Assumed constants
NUM_PLATE_MAX_LENGTH = 20
MAX_YEAR_DELTA_FOR_PARKING_EVENT = 50


class VehicleCategory(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"


class ParkingEventType(Enum):
    ENTER = "Enter"
    EXIT = "Exit"


class ParkingSystemResponseType(Enum):
    ACCPET = "Accept"
    REJECT = "Reject"


DB_VEHICLE_CATEGORY_CONSTRAINT_CHECK_STRING = (
    "vehicle_category == "
    + "'"
    + str(VehicleCategory.MOTORCYCLE.value)
    + "'"
    + " OR vehicle_category == "
    + "'"
    + str(VehicleCategory.CAR.value)
    + "'"
)
