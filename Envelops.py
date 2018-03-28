def input_text(text):
    return input(text)


def is_possible_to_fit(rectangle1, rectangle2):
    """Compare rectangles.

    :param rectangle1: (dict)should contain keys "side1" and "side2"
    :param rectangle2: (dict)should contain keys "side1" and "side2"
    :return: (bool)True if it`s possible to fit rectangle2 in rectangle1,
             False otherwise.

    """
    rectangle1, rectangle2 = sort_envelops(rectangle1, rectangle2)
    if (is_sqrt_sides_greater(rectangle1, rectangle2) and
        is_sum_sides_bigger(rectangle1, rectangle2) and
            is_min_side_bigger(rectangle1, rectangle2)):
        return True
    else:
        return False


def is_sqrt_sides_greater(rectangle1, rectangle2):
    """Compare sums of squared sizes.

    :param rectangle1: (dict)should contain keys "side1" and "side2"
    :param rectangle2: (dict)should contain keys "side1" and "side2"
    :return: (bool)True if sum of squared sizes rectangle1 greater
             the sum of squared sizes rectangle2,
             False otherwise.

    """
    if rectangle1["side1"]**2 + rectangle1["side2"]**2 > \
            rectangle2["side1"]**2 + rectangle2["side2"]:
        return True
    else:
        return False


def is_sum_sides_bigger(rectangle1, rectangle2):
    """Compare sides sums.

    :param rectangle1: (dict)should contain keys "side1" and "side2"
    :param rectangle2: (dict)should contain keys "side1" and "side2"
    :return: (bool)True if sides sums rectangle1 greater then
              sides sums rectangle2,
              False otherwise.
    """
    if sum(rectangle1) > sum(rectangle2):
        return True
    else:
        return False


def is_min_side_bigger(rectangle1, rectangle2):
    """Compare min sides of rectangles.

    :param rectangle1: (dict)should contain keys "side1" and "side2"
    :param rectangle2: (dict)should contain keys "side1" and "side2"
    :return: (bool)True if min side of rectangle1 greater then
              min side of rectangle2,
              False otherwise.

    """
    if min(rectangle1["side1"], rectangle1["side2"]) > \
            min(rectangle2["side1"], rectangle2["side2"]):
        return True
    else:
        return False


def sort_envelops(rectangle1, rectangle2):
    """Sort two rectangles by squares.

    :param rectangle1: (dict)should contain keys "side1" and "side2"
    :param rectangle2: (dict)should contain keys "side1" and "side2"
    :return: (tuple):[0](dict) - rectangle with a greater square
                     [1](dict) - rectangle with a smaller square

    """
    if rectangle1["side1"] * rectangle1["side2"] < \
            rectangle2["side1"] * rectangle2["side2"]:
        return rectangle2, rectangle1
    else:
        return rectangle1, rectangle2


def validate_side(side):
    """Validate side of rectangle.

    :param side:(str)side to validate
    :return:(float)side if it's float and greater then 0.
             Otherwise ask to input valid value.

    """
    success = False
    while not success:
        try:
            side = float(side)
            success = True
        except ValueError:
            side = input_text("Wrong! Parameter should be float.\nTry again:")
            continue
        if side <= 0:
            side = input_text("Wrong! Parameters should be bigger then 0.\nTry again:")
            success = False
    return side


def input_parameters():
    """Input parameters.

    :return: (tuple):[0](dict) - rectangle1 with keys "side1" and "side2" and valid values
                     [1](dict) - rectangle2 with keys "side1" and "side2" and valid values

    Request to enter value of sides one at the time.
    """
    print("Enter first envelop parameters:")
    side_1 = validate_side(input_text("Side 1:"))
    side_2 = validate_side(input_text("Side 2:"))
    rectangle1 = {"side1": side_1, "side2": side_2}
    print("Enter second envelop parameters:")
    side_1 = validate_side(input_text("Side 1:"))
    side_2 = validate_side(input_text("Side 2:"))
    rectangle2 = {"side1": side_1, "side2": side_2}
    return rectangle1, rectangle2


if __name__ == "__main__":
    one_more = True
    while one_more:
        first_envelop, second_envelop = input_parameters()
        if is_possible_to_fit(first_envelop, second_envelop):
            print("Possible")
        else:
            print("Impossible")
        answer = input("Do you want to continue?").lower()
        if answer != "yes" and answer != "y":
            one_more = False
