from parking_system.utility.constants import *
import re
from parking_system.utility.error_utilities import *


def is_valid_num_plate(num_plate):
    """
    Validates number plate format
    """

    if (
        len(num_plate) > 0
        and len(num_plate) <= NUM_PLATE_MAX_LENGTH
        and re.match("^[A-Za-z0-9]*$", num_plate)
    ):
        return True
    else:
        return False


def is_valid_timestamp(timestamp):
    """
    Validates timestamp format and range
    """

    if timestamp.isdigit():
        from datetime import datetime

        event_year = datetime.utcfromtimestamp(int(timestamp)).year
        current_year = datetime.utcnow().year
        if event_year > (
            current_year - MAX_YEAR_DELTA_FOR_PARKING_EVENT
        ) and event_year < (current_year + MAX_YEAR_DELTA_FOR_PARKING_EVENT):
            return True
        else:
            return False
    else:
        return False


def validate_enter_event(enter_event):
    """
    Validates parking enter event attributes
    """

    if not isinstance(enter_event, list):
        raise InvalidInputError("Incorrect entry input format", enter_event)
    elif len(enter_event) < 2:
        raise MissingInputParameterError("Missing vehicle category information")
    elif len(enter_event) < 3:
        raise MissingInputParameterError("Missing number plate information")
    elif len(enter_event) < 4:
        raise MissingInputParameterError("Missing entry timestamp information")
    elif enter_event[1] not in [
        str(VehicleCategory.CAR.value),
        str(VehicleCategory.MOTORCYCLE.value),
    ]:
        raise InvalidInputError("Incorrect vehicle category", enter_event[1])
    elif not (is_valid_num_plate(enter_event[2])):
        raise InvalidInputError("Incorrect number plate", enter_event[2])
    elif not (is_valid_timestamp(enter_event[3])):
        raise InvalidInputError("Incorrect entry timestamp", enter_event[3])


def validate_exit_event(exit_event):
    """
    Validates parking exit event attributes
    """

    if not isinstance(exit_event, list):
        raise InvalidInputError("Incorrect exit input format", exit_event)
    elif len(exit_event) < 2:
        raise MissingInputParameterError("Missing number plate information")
    elif len(exit_event) < 3:
        raise MissingInputParameterError("Missing entry timestamp information")
    elif not (is_valid_num_plate(exit_event[1])):
        raise InvalidInputError("Incorrect number plate", exit_event[1])
    elif not (is_valid_timestamp(exit_event[2])):
        raise InvalidInputError("Incorrect entry timestamp", exit_event[2])


def validate_slot_allotment_event(allotment_event):
    """
    Validates slot allotment event attributes
    """

    allotments = allotment_event.split()
    if len(allotments) and len(allotments) != 2:
        raise InvalidAllotmentError(
            "Incorrect allotment event. Two allotments expected."
        )
    for allotment in allotments:
        if not allotment.isdigit():
            raise InvalidAllotmentError(
                "Incorrect allotment event. Expected numerical allotments."
            )
