import re
import sys


def open_file(file_path, attr="r"):
    """Open file."""
    return open(file_path, attr)


def count_substrings(string, file_path):
    try:
        with open_file(file_path) as in_file:
            result = re.findall(string, in_file.read(), re.IGNORECASE)
            return len(result)
    except FileNotFoundError:
        return "File not found."


def replace_substring(string, new_string, file_path):
    try:
        with open(file_path) as file:
            file_text = file.read()
        with open(file_path, "w") as file:
            file.write(re.sub(string, new_string, file_text, re.IGNORECASE))
        return "Done!"
    except FileNotFoundError:
        return "File not found."


def validate(args):
    if len(args) == 3:
        result_substrings = count_substrings(args[2], args[1])
        if type(result_substrings) == int:
            return "Result is " + str(result_substrings)
        else:
            return result_substrings
    elif len(args) == 4:
        return replace_substring(args[2], args[3], args[1])
    else:
        return "Enter file path and string for counting.\nOr enter file path, " \
               "search string and new value for replacement."


if __name__ == "__main__":
    func_result = validate(sys.argv)
    print(func_result)
