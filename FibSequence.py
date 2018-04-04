import sys


def validate_args(args):
    """
    Validate arguments.

    :param list args: command lime arguments
    :return tuple or str: min_limit(int) - first command line argument
            if it's integer and greater then 0
            max_limit(int) - second command line argument
            if it's integer and greater then 0
            string with the reason of invalid value
    """
    if len(args) == 2:
        try:
            min_limit = int(args[0])
            max_limit = int(args[1])
        except ValueError:
            return False, "Invalid arguments. Limits should be integer."
        else:
            if min_limit > 0 and max_limit > 0:
                return min_limit, max_limit
            else:
                return False, "Invalid arguments. Limits should be positive."
    else:
        return False, "Enter two positive limits to generate a sequence."


def get_fib_sequence(minimum, maximum):
    """
    Calculate Fibonacci sequence for the range.

    :param int minimum: min limit fo sequence
    :param int maximum: max limit foe sequence
    :return str: Fibonacci sequence for the range, separated comma
    """
    curr = 1
    previous = 0
    result = []
    while curr < maximum:
        if curr > minimum:
            result.append(curr)
        previous, curr = curr, (curr + previous)
    return ", ".join(map(str, result))


if __name__ == "__main__":
    validation_result = validate_args(sys.argv[1:])
    if not validation_result[0]:
        print(validation_result[1])
    else:
        print(get_fib_sequence(*validation_result))
