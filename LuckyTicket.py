from NumberComb import number_of_combinations


def choose_algorithm(alg_name, number):
    if alg_name == "Moscow" or "Peter":
        return moscow_algorithm(number)
    else:
        print("algorithm doesn't exist!")


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
    try:
        with open("LuckyTicketsAlgorithm.txt") as file:
            name = file.read()
            return name
    except FileNotFoundError:
        print("File not found.")


def get_number_of_digits():
    print("Enter number of digits:")
    try:
        number = int(input())
    except ValueError:
        print("Wrong! Number should be integer.")
    else:
        if number in (2, 4, 6, 8):
            return number
        else:
            print("Wrong! Number should be even, less then 10 and not 0.")


if __name__ == "__main__":
    algorithm_name = get_algorithm_name()
    number_of_digits = get_number_of_digits()
    print(choose_algorithm(algorithm_name, number_of_digits // 2))
