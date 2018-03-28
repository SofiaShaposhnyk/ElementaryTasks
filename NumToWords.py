import sys
from numberNames import ones, tens, hundreds, other


result = []


def get_form(digits, index):
    index = int(index / 3)
    if other[index] == "":
        return ""
    elif digits["ones"] == 1 and digits["tens"] != 1:
        if index == 1:
            return other[index][0]
        return other[index]
    elif 2 <= digits["ones"] <= 4 and digits["tens"] != 1:
        if index == 1:
            return other[index][2]
        return other[index] + "а"
    else:
        if index == 1:
            return other[index][1]
        else:
            return other[index] + "ов"


def get_numeral(number, position1, position2):
    return (number % 10**position1) // 10**position2


def get_digits(number, position):
    digits = dict()
    digits["ones"] = get_numeral(number, position + 1, position)
    digits["tens"] = get_numeral(number, position + 2, position + 1)
    digits["hundreds"] = get_numeral(number, position + 3, position + 2)
    return digits


def append_digits(digits):
    tens_and_ones = digits["tens"] * 10 + digits["ones"]
    if tens_and_ones < 20:
        result.append(ones[tens_and_ones])
    else:
        result.append(ones[digits["ones"]])
        result.append(tens[digits["tens"]])
    result.append(hundreds[digits["hundreds"]])


def to_words(number):
    count_numbers = len(number)
    number = int(number)
    position = 0
    while position < count_numbers:
        digits = get_digits(number, position)
        result.append(get_form(digits, position))
        if digits["ones"] == (1 or 2) and int(position / 3) == 1:
            if digits["ones"] == 1:
                result.append("одна")
            elif digits["ones"] == 2:
                result.append("две")
        else:
            append_digits(digits)
            position += 3
    result.reverse()


def validate_args(args):
    if len(args) > 1:
        try:
            number = int(args[1])
        except ValueError:
            return False, "Enter a number."
        else:
            if number > 0:
                if len(args[1]) < 97:
                    return True, args[1]
                else:
                    return False, "Too long number."
            else:
                return False, "Invalid argument. Number should be bigger then 0."
    else:
        return False, "Enter a number to convert."


if __name__ == "__main__":
    validation_result = validate_args(sys.argv)
    if validation_result[0]:
        to_words(validation_result[1])
        print(" ".join(result))
    else:
        print(validation_result[1])
