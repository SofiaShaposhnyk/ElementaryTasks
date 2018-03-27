from NumberComb import number_of_combinations


def get_input(text):
    return input(text)


def choose_algorithm(alg_name, number):
    if alg_name == "Moscow" or alg_name == "Peter":
        return moscow_algorithm(number)
    else:
        return "Algorithm doesn't exist!"


def moscow_algorithm(number):
    result = 0
    curr_number_of_combinations = number_of_combinations[number - 1]
    if number % 2 == 1:
        for i in range(len(curr_number_of_combinations)):
            result += curr_number_of_combinations[i]**2
        return result * 2
    else:
        for i in range(len(curr_number_of_combinations) - 1):
            result += curr_number_of_combinations[i] ** 2
        result *= 2
        last_element = (curr_number_of_combinations[(number * 9) // 2])
        result += last_element**2
        return result


def get_algorithm_name():
    file_path = get_input("Enter path to file with algorithm name:")
    with open(file_path) as file:
        name = file.read()
        return name


def get_number_of_digits():
    try:
        number = int(get_input("Enter number of digits:"))
    except ValueError:
        return "Wrong! Number should be integer."
    else:
        if number in (2, 4, 6, 8):
            return number
        else:
            return "Wrong! Number should be even, less then 10 and not 0."


if __name__ == "__main__":
    try:
        algorithm_name = get_algorithm_name()
    except FileNotFoundError:
        print("File not found")
    else:
        number_of_digits = get_number_of_digits()
        if type(number_of_digits) == int:
            print(choose_algorithm(algorithm_name, number_of_digits // 2))
        else:
            print(number_of_digits)
