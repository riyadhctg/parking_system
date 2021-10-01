# Parking System
This parking system application takes input to generate parking slots and events. Parking events are then consumed by the application to park cars and motorcycles for an hourly fee.

## Assumptions
 - Max length of number plate of 20
 - Number plate IDs are unique
 - A valid parking event timestamp is between the range of last 50 years and next 50 years relative to current date


## Project Structure
- Structure of this project is inspired by [Route-Controller-Service](https://sodocumentation.net/node-js/topic/10785/route-controller-service-structure-for-expressjs)
- Test cases are within `test` folder
- `utility` folder contains various helper functions

```bash
📦project_directory
┣ 📂parking_system
┃ ┣ 📂controller
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜allocate_slots.py
┃ ┃ ┣ 📜park_vehicle.py
┃ ┃ ┗ 📜unpark_vehicle.py
┃ ┣ 📂model
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜db_init.py
┃ ┃ ┣ 📜parking_record.py
┃ ┃ ┗ 📜slot.py
┃ ┣ 📂route
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜router.py
┃ ┃ ┗ 📜routes.py
┃ ┣ 📂service
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜parking_record_service.py
┃ ┃ ┗ 📜slot_service.py
┃ ┣ 📂test
┃ ┃ ┣ 📂mock_data
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┗ 📜test_cases.py
┃ ┣ 📂utility
┃ ┃ ┣ 📜__init__.py
┃ ┃ ┣ 📜constants.py
┃ ┃ ┣ 📜error_utilities.py
┃ ┃ ┣ 📜helper_functions.py
┃ ┃ ┣ 📜input_preprocessor.py
┃ ┃ ┣ 📜input_validator.py
┃ ┃ ┗ 📜logger.py
┃ ┣ 📜__init__.py
┃ ┣ 📜__main__.py
┃ ┗ 📜app.py
┣ 📜Dockerfile
┣ 📜LICENSE
┣ 📜README.md
┣ 📜example_input.txt
┗ 📜requirements.txt
```

## Installation
- To avoid potential version / compatibility issue, running it inside docker is recommended.
- Please note that running the some of the commands using `sudo` may be required depending on the logged in user / permission. 

```
# install docker
apt install -y docker.io

# navigate to the project directory i.e. the location of this README.md file
cd <path/to/project>

# Build docker image (note trailing dot (.), which is important)
docker build --tag parking-system-riyadh .

```

## How to run - basic
 - The following command will run the application with default input provided with the assignment. It is stored at project root as example_input.txt
```
# Run docker image - this will run the 
dokcer run parking-system-riyadh
```
- If we want to make changes to the code and test, then `docker build` command from above needs to be run again

## How to run - advanced
- In the basic method, the container runs the application and then exits. It shows the output for default input on the console. This method shows how to run the application from within the container
```
# To keep the container running
docker run -d parking-system-riyadh tail -f /dev/null

# The above command will output a string. Copy the string and use it in the next command
docker exec -it <copied-string> sh

# Now we should be inside the container. Run the following command to run the application with the default input
python3 -m parking_system example_input.txt

# Run test cases
python3 -m unittest discover -v  
```
- Using this method, we can quickly make changes to the code and test, using `vi`.
