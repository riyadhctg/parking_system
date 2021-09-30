from parking_system.controller.unpark_vehicle import unpark_vehicle
from parking_system.controller.park_vehicle import park_vehicle
from parking_system.controller.allocate_slots import allocate_slots
from parking_system.route.routes import Routes
from parking_system.utility.logger import logger


def route_requests(route, request):
    """
    Routes request based on the route passed
    """

    logger.info("%s request received", route)
    if route == str(Routes.ALLOCATE_SLOTS.value):
        allocate_slots(request)
    elif route == str(Routes.PARK_VEHICLE.value):
        park_vehicle(request)
    elif route == str(Routes.UNPARK_VEHICLE.value):
        unpark_vehicle(request)
    else:
        logger.error("Unknown request")
        raise ValueError("Unknown request")
