from parking_system.utility.input_validator import (
    validate_enter_event,
    validate_exit_event,
    validate_slot_allotment_event,
)
from parking_system.utility.constants import *
from parking_system.utility.error_utilities import *
from parking_system.utility.logger import logger


def create_parking_event(input):
    """
    Creates a parking event dict from text input
    """

    event_details = input.split()
    event_object = None

    try:
        if event_details[0] == ParkingEventType.ENTER.value:
            validate_enter_event(event_details)
            event_object = {
                "parking_event_type": ParkingEventType.ENTER.value,
                "vehicle_category": event_details[1],
                "num_plate": event_details[2],
                "timestamp": int(event_details[3]),
            }
        elif event_details[0] == ParkingEventType.EXIT.value:
            validate_exit_event(event_details)
            event_object = {
                "parking_event_type": ParkingEventType.EXIT.value,
                "num_plate": event_details[1],
                "timestamp": int(event_details[2]),
            }
        else:
            raise InvalidInputError("Unknown parking event type", event_details[0])
    except InvalidInputError as e:
        logger.error(e)
        return None
    except MissingInputParameterError as e:
        logger.error(e)
        return None
    except Exception as e:
        raise Exception("An error occured while creating the parking event", e)

    return event_object


def parse_inputs(input_file):
    """
    Parses text input for parking system
    """

    slot_allotments = None
    parking_events = []

    try:
        with open(input_file) as file:
            for idx, val in enumerate(file):
                if idx == 0:
                    validate_slot_allotment_event(val)
                    slot_allotments = [int(n) for n in val.split()]
                else:
                    formatted_parking_event = create_parking_event(val.rstrip())
                    if formatted_parking_event is not None:
                        parking_events.append(formatted_parking_event)
    except InvalidAllotmentError as e:
        logger.error(e)
        raise e
    except Exception as e:
        logger.error("An error occured while parsing the input file" + str(e))
        raise Exception("An error occured while parsing the input file", e)

    return slot_allotments, parking_events
