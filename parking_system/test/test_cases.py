from parking_system.utility.constants import LOGGER_NAME
import unittest
from parking_system.app import run
from parking_system.utility.error_utilities import *
from parking_system.model.db_init import db
import io
import os
from contextlib import redirect_stdout


class TestParkingSystem(unittest.TestCase):
    def setUp(self):
        os.environ["DB_CONNECTION_STRING"] = ":memory:"

    def tearDown(self):
        os.environ.pop("DB_CONNECTION_STRING")
        db.close()

    def clean_up_after_every_test_case_run(self):
        db.close()

    def test_correctly_handles_default_example_inputs_and_outputs(self):
        output_file = open("parking_system/test/mock_data/example_output.txt")
        output_file_content = output_file.read()
        f = io.StringIO()
        with redirect_stdout(f):
            run("./example_input.txt")
        output_generated_by_parking_system_app = f.getvalue()
        self.assertEqual(output_generated_by_parking_system_app, output_file_content)
        output_file.close()
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_vehicle_category(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/incorrect_vehicle_category.txt")
        self.assertIn("Incorrect vehicle category", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_parking_event_type(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run(
                "./parking_system/test/mock_data/incorrect_parking_event_input_type.txt"
            )
        self.assertIn("Unknown parking event type", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_number_plate_format(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/incorrect_entry_num_plate.txt")
        self.assertIn("Incorrect number plate", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_entry_timestamp(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/incorrect_entry_timestamp.txt")
        self.assertIn("Incorrect entry timestamp", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_exit_timestamp(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/incorrect_exit_timestamp.txt")
        self.assertIn("Incorrect entry timestamp", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_incorrect_parking_slot_allotments(self):
        with self.assertRaises(InvalidAllotmentError):
            f = io.StringIO()
            with redirect_stdout(f):
                run(
                    "./parking_system/test/mock_data/incorrect_parking_slot_allotment.txt"
                )
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_missing_entry_event_parameter(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/missing_entry_event_parameters.txt")
        self.assertIn("Missing entry timestamp information", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_missing_exit_event_parameter(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/missing_exit_event_parameters.txt")
        self.assertIn("Missing entry timestamp information", str(cm.output))
        self.clean_up_after_every_test_case_run()

    def test_correctly_handles_input_with_older_exit_timestamp(self):
        with self.assertLogs(LOGGER_NAME, level="ERROR") as cm:
            run("./parking_system/test/mock_data/older_exit_timestamp.txt")
        self.assertIn("Exit time cannot be older than entry time", str(cm.output))
        self.clean_up_after_every_test_case_run()


if __name__ == "__main__":
    unittest.main()
