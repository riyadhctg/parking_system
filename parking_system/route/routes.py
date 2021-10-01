from enum import Enum


class Routes(Enum):
    """
    All available routes included in this class
    """

    ALLOCATE_SLOTS = "allocate_slots"
    PARK_VEHICLE = "park_vehcile"
    UNPARK_VEHICLE = "unpark_vehicle"
