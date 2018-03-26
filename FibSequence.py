import sys


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
    if len(sys.argv) == 3:
        try:
            min_limit = int(sys.argv[1])
            max_limit = int(sys.argv[2])
        except ValueError:
            print("Invalid arguments. Limits should be integer.")
        else:
            if min_limit > 0 and max_limit > 0:
                print(get_fib_sequence(int(sys.argv[1]), int(sys.argv[2])))
            else:
                print("Invalid arguments. Limits should be positive.")
    else:
        print("Enter two positive limits to generate a sequence.")
