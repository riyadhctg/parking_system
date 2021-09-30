# Parking System

This parking system application takes input to generate parking slots and events. Parking events are then consumed by the application to park cars and motorcycles for an hourly fee.

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

