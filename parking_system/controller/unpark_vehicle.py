from parking_system.utility.error_utilities import InvalidInputError
from parking_system.service.parking_record_service import (
    get_parking_record,
    update_parking_record_with_exit_time,
)
from parking_system.service.slot_service import update_slot
from parking_system.utility.helper_functions import calculate_fee
from parking_system.utility.logger import logger


def unpark_vehicle(event):
    """
    Removes current parked vehicle based on the number plate
    """

    num_plate = event["num_plate"]
    exit_time = event["timestamp"]
    try:
        parking_record = get_parking_record(num_plate)
        if exit_time < parking_record.entered:
            raise InvalidInputError("Exit time cannot be older than entry time")

        slot_id = parking_record.slot_id
        fee = calculate_fee(
            parking_record.entered, exit_time, parking_record.vehicle_category
        )
        update_parking_record_with_exit_time(num_plate, exit_time)
        update_slot(slot_id, True)
        print(slot_id, fee)
    except InvalidInputError as e:
        logger.error(e)
        raise e
    except Exception as e:
        logger.error(
            "An error occurred while processing unpark_vehicle request", str(e)
        )
        raise Exception("An error occurred while processing unpark_vehicle request", e)
