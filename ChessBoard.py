import sys


def get_board(horizontal, vertical):
    result = ""
    for ver in range(vertical):
        line = ""
        for hor in range(horizontal):
            if (ver + hor) % 2 == 0:
                line += "*"
            else:
                line += " "
        result += (line + "\n")
    return result


def convert(str_type):
    try:
        int_type = int(str_type)
        return int_type
    except ValueError:
        return False


def print_chess_board(horizontal, vertical):
    horizontal = convert(horizontal)
    vertical = convert(vertical)
    if horizontal and vertical:
        if horizontal > 0 and vertical > 0:
            return get_board(horizontal, vertical)
        else:
            return "Chessboard sizes should be positive."
    else:
        return "Wrong! It should be integer numbers."


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(print_chess_board(sys.argv[1], sys.argv[2]))
    else:
        print("Enter chessboard size. It should be two integer numbers.")
