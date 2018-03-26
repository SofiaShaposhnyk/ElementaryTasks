import re
import sys


def count_substrings(string, file_path):
    try:
        with open(file_path) as in_file:
            result = re.findall(string, in_file.read(), re.IGNORECASE)
            result = len(result)
    except FileNotFoundError:
        print("File not found.")
        return False
    return result


def replace_substring(string, new_string, file_path):
    try:
        with open(file_path) as file:
            file_text = file.read()
        with open(file_path, "w") as file:
            file.write(re.sub(string, new_string, file_text, re.IGNORECASE))
        print("Done!")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        if len(sys.argv) == 3:
            number_substrings = count_substrings(sys.argv[2], sys.argv[1])
            if number_substrings:
                print("Result is", number_substrings)
        elif len(sys.argv) == 4:
            replace_substring(sys.argv[2], sys.argv[3], sys.argv[1])
    else:
            print("Enter file path and string for counting.\nOr enter file path, "
                  "search string and new value for replacement.")
