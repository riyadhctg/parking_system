from dotenv import load_dotenv

load_dotenv()
from parking_system.utility.error_utilities import InvalidInputError
from parking_system.utility.constants import ParkingEventType
from parking_system.model.slot import Slot
from parking_system.model.parking_record import ParkingRecord
from parking_system.model.db_init import db
from parking_system.utility.input_preprocessor import parse_inputs
from parking_system.utility.logger import logger
from parking_system.route.router import route_requests
from parking_system.route.routes import Routes


def submit_event_to_router(event):
    """
    Submits event to router for further processing
    """

    if event["parking_event_type"] == ParkingEventType.ENTER.value:
        route_requests(str(Routes.PARK_VEHICLE.value), event)
    elif event["parking_event_type"] == ParkingEventType.EXIT.value:
        route_requests(str(Routes.UNPARK_VEHICLE.value), event)


def setup_database():
    """
    Sets up database connection and creates tables
    """

    try:
        db.connect()
        db.create_tables([Slot, ParkingRecord])
        logger.info("Database table created successfully")
    except Exception as e:
        logger.error("An error occurred while initializing database" + str(e))
        raise Exception("An error occurred while initializingdatabase", e)


def run(input_file):
    """
    Runs the parking system application
    """

    inputs = parse_inputs(input_file)
    slot_allotments, parking_events = inputs
    setup_database()
    route_requests(str(Routes.ALLOCATE_SLOTS.value), slot_allotments)
    for event in parking_events:
        try:
            submit_event_to_router(event)
        except InvalidInputError as e:
            logger.warning(
                "Invalid input event. Skipping this and continuing with the next request "
                + str(e)
            )
        except Exception as e:
            logger.error(e)
            raise e
    db.close()
