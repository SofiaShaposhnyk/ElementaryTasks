import sys


def validate_args(args):
    """Validate arguments.

    :param args: (list)command lime arguments
    :return: (tuple)min_limit(int) - first command line argument
                    if it's integer and greater then 0
                    max_limit(int) - second command line argument
                    if it's integer and greater then 0
             (str)reason of invalid value

    """
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
    """Calculate Fibonacci sequence for the range.

    :param minimum: (int)min limit fo sequence
    :param maximum: (int)max limit foe sequence
    :return: (str)Fibonacci sequence for the range, separated comma
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
    validation_result = validate_args(sys.argv)
    if type(validation_result) == str:
        print(validation_result)
    else:
        print(get_fib_sequence(*validation_result))
