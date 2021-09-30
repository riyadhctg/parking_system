from parking_system.utility.error_utilities import InvalidInputError
from parking_system.service.parking_record_service import (
    select_parking_record,
    insert_parking_record,
)
from parking_system.service.slot_service import update_slot, select_available_slots
from parking_system.utility.constants import *
from parking_system.utility.logger import logger


def park_vehicle(parking_event):
    """
    Parks vehcile based on the vehicle category and slot availability
    """

    num_plate = parking_event["num_plate"]
    time_stamp = parking_event["timestamp"]
    vehicle_category = parking_event["vehicle_category"]

    try:
        parking_record = select_parking_record(num_plate)
        if parking_record.exists():
            raise InvalidInputError(
                "A vehicle with the same number plate {} already exists".format(
                    num_plate
                )
            )
        available_slots = select_available_slots(vehicle_category)
        if available_slots and available_slots[0] is not None:
            slot_id = available_slots[0]
            update_slot(slot_id, False)
            insert_parking_record(vehicle_category, num_plate, time_stamp, slot_id)
            print(ParkingSystemResponseType.ACCPET.value, slot_id)
        else:
            print(ParkingSystemResponseType.REJECT.value)
    except InvalidInputError as e:
        logger.error(e)
        raise e
    except Exception as e:
        logger.error("An error occurred while processing park_vehicle request" + str(e))
        raise Exception("An error occurred while processing park_vehicle request", e)
