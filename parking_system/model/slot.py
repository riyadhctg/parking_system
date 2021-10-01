import peewee
from parking_system.utility.constants import (
    DB_VEHICLE_CATEGORY_CONSTRAINT_CHECK_STRING,
    NUM_PLATE_MAX_LENGTH,
)
from parking_system.model.db_init import db


class Slot(peewee.Model):
    """
    Slot schema defintion
    """

    id = peewee.CharField(NUM_PLATE_MAX_LENGTH, unique=True)
    vehicle_category = peewee.CharField(
        constraints=[peewee.Check(DB_VEHICLE_CATEGORY_CONSTRAINT_CHECK_STRING)]
    )
    is_available = peewee.BooleanField(default=True)

    class Meta:

        database = db
