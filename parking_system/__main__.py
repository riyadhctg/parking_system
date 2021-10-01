import sys
from parking_system import app

if __name__ == "__main__":
    try:
        input = sys.argv[1]
    except Exception as e:
        raise Exception("Missing input file", e)
    app.run(input)
