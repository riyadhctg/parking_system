from parking_system.model.slot import Slot


def select_available_slots(vehicle_category):
    """
    Selects available slots
    """
    
    return Slot.select().where(
        (Slot.vehicle_category == vehicle_category) & (Slot.is_available == True)
    )


def create_slots(all_slots):
    """
    Bulk create slots
    """

    create_slots = Slot.insert_many(all_slots)
    create_slots.execute()


def update_slot(slot_id, is_available):
    """
    Updates slot's availability status
    """

    update_query = Slot.update(is_available=is_available).where(Slot.id == slot_id)
    update_query.execute()
