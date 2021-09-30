# Automated Valet Car Parking Backend

Automated Valet Car Parking Backend takes input from a text file to generate parking slots and events. Each vehicle upon entry can only park in a lot available for that vehicle type. If there are no lots available for that vehicle type, it should be denied an entry into the space.

All the lots in the parking space can be considered as being distinctly numbered eg: CarLot1, CarLot2,..., MotorcycleLot1, MotorcycleLot2,.... Each vehicle upon entering is allotted to the lot with the lowest number for that vehicular type eg: a car entering a parking space with the available lots CarLot2, CarLot4, CarLot5 would be assigned to CarLot2.

When a vehicle wants to exit the car park, the system will return the parking lot that the vehicle will be removed from and charge them an appropriate parking fee (rounded up to the nearest hour, i.e., 1hr 1min is charged as 2hr): $1/hour for a motorcycle and $2/hour for a car.


## Assumptions

 - Max length of number plate of 20
 - Number plate IDs are unique
 - A valid parking event timestamp is between the range of last 50 years and next 50 years relative to current date

## Installation

 - [Pipenv](https://pypi.org/project/pipenv/) is used for dependency management. 
 - Default input is stored in a text file named `example_input.txt` in the project directory 

```
pip install pipenv
pipenv install
```

## How to run
```
pipenv run python -m parking_system example_input.txt
```

## How to test
```
pipenv run python -m  unittest discover -v
```

