from parking_system import app
import sys

if __name__ == "__main__":
    try:
        input = sys.argv[1]
    except Exception as e:
        raise Exception("Missing input file", e)
    app.run(input)
