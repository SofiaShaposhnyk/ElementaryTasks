import sys
import math


def validate(args):
    if len(args) == 2:
        try:
            limit = int(args[1])
        except ValueError:
            return "Limit should be integer."
        else:
            if limit > 0:
                return limit
            else:
                return "Limit should be positive."
    else:
        return "Enter one number to generate a sequence."


def get_sequence(number):
    limit = int(math.sqrt(number))
    return ", ".join(map(str, tuple(range(0, limit + 1, 1))))


if __name__ == "__main__":
    validation_result = validate(sys.argv)
    if type(validation_result) == int:
        print(get_sequence(validation_result))
    else:
        print(validation_result)
