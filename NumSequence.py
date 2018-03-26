import sys
import math


def get_sequence(n):
    try:
        limit = int(math.sqrt(int(n)))
    except ValueError:
        print("Invalid argument. Enter a number.")
        return False
    return ", ".join(map(str, tuple(range(0, limit + 1, 1))))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        result = get_sequence(sys.argv[1])
        if result:
            print(result)
    else:
        print("Enter a number to generate a sequence.")
