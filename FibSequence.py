import sys


def validate_args(args):
    if len(args) == 3:
        try:
            min_limit = int(args[1])
            max_limit = int(args[2])
        except ValueError:
            return "Invalid arguments. Limits should be integer."
        else:
            if min_limit > 0 and max_limit > 0:
                return min_limit, max_limit
            else:
                return "Invalid arguments. Limits should be positive."
    else:
        return "Enter two positive limits to generate a sequence."


def get_fib_sequence(minimum, maximum):
    curr = 1
    previous = 0
    result = []
    while curr < maximum:
        if curr > minimum:
            result.append(curr)
        previous, curr = curr, (curr + previous)
    return ", ".join(map(str, result))


if __name__ == "__main__":
    validation_result = validate_args(sys.argv)
    if type(validation_result) == str:
        print(validation_result)
    else:
        print(get_fib_sequence(*validation_result))
