from parking_system.utility.error_utilities import InvalidInputError
from parking_system.model.parking_record import ParkingRecord


def select_parking_record(num_plate):
    """
    Selects parking record
    """

    return ParkingRecord.select().where(
        (ParkingRecord.num_plate == num_plate) & (ParkingRecord.exited == None)
    )


def get_parking_record(num_plate):
    """
    Gets parking record
    """

    query = select_parking_record(num_plate)
    if not query.exists():
        raise InvalidInputError(
            "Parking record not found for vehicle with number plate: ", num_plate
        )
    else:
        return query.get()


def insert_parking_record(vehicle_category, num_plate, time_stamp, slot_id):
    """
    Creates parking record
    """

    vehicle = ParkingRecord.create(
        vehicle_category=vehicle_category,
        num_plate=num_plate,
        entered=time_stamp,
        slot_id=slot_id,
    )
    vehicle.save()


def update_parking_record_with_exit_time(num_plate, exit_time):
    """
    Update existing parking record with exit time
    """

    update_query = ParkingRecord.update(exited=exit_time).where(
        (ParkingRecord.num_plate == num_plate) & (ParkingRecord.exited == None)
    )
    update_query.execute()
