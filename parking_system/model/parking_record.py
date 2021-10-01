import peewee
from parking_system.utility.constants import (
    NUM_PLATE_MAX_LENGTH,
    DB_VEHICLE_CATEGORY_CONSTRAINT_CHECK_STRING,
)
from parking_system.model.db_init import db


class ParkingRecord(peewee.Model):
    """
    ParkingRecord schema definition
    """

    num_plate = peewee.CharField(NUM_PLATE_MAX_LENGTH)
    vehicle_category = peewee.CharField(
        constraints=[peewee.Check(DB_VEHICLE_CATEGORY_CONSTRAINT_CHECK_STRING)]
    )
    entered = peewee.IntegerField()
    exited = peewee.IntegerField(null=True, default=None)
    fee = peewee.IntegerField(null=True, default=None)
    slot_id = peewee.CharField(NUM_PLATE_MAX_LENGTH)

    class Meta:

        database = db
