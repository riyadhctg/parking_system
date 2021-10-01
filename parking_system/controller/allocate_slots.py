from parking_system.service.slot_service import create_slots
from parking_system.utility.constants import VehicleCategory
from parking_system.utility.helper_functions import create_slot_object_list
from parking_system.utility.logger import logger


def allocate_slots(allotments):
    """
    Creates slots for the parking system
    """

    all_slots = []
    try:
        car_slots = create_slot_object_list(VehicleCategory.CAR.value, allotments[0])
        motorcycle_slots = create_slot_object_list(
            VehicleCategory.MOTORCYCLE.value, allotments[1]
        )
        all_slots = car_slots + motorcycle_slots
        create_slots(all_slots)
    except Exception as e:
        logger.error(
            "An error occurred while processing allocate_slots request" + str(e)
        )
        raise Exception("An error occurred while processing allocate_slots request", e)
