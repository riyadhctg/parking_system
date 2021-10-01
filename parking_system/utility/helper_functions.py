from parking_system.utility.constants import VehicleCategory


def create_slot_object_list(category, quantity):
    """
    Creates slots with unique IDs based on the allotment
    """

    slots = []
    for num in range(quantity):
        id = str(category).title() + "Lot" + str(num + 1)
        slot_object = {"id": id, "vehicle_category": str(category)}
        slots.append(slot_object)
    return slots


def calculate_fee(entry_time, exit_time, vehicle_category):
    """
    Calculates parking fee based on exit and entry time at $1 per hour.
    Any fraction of hour is considered a full hour for billing purposes.
    """

    duration = exit_time - entry_time
    duration_in_hour = int(duration / (60 * 60))
    fee = None
    if duration % (60 * 60) != 0:
        duration_in_hour = duration_in_hour + 1

    if vehicle_category == VehicleCategory.CAR.value:
        fee = duration_in_hour * 2
    elif vehicle_category == VehicleCategory.MOTORCYCLE.value:
        fee = duration_in_hour * 1

    return fee
