import re
from Triangle import Triangle


def input_text(text):
    return input(text)


def input_parameters():
    """Input and validate parameters.

    :return: tuple: side1(float), side2(float), side3(float) - valid sides for triangle
             tuple: False, str - reason of invalid values

    """
    triangle_parameters = re.sub(" ", "",
                                 input_text("Input triangle parameters:")).lower().split(",")
    if len(triangle_parameters) == 4:
        name = triangle_parameters[0]
        try:
            side1, side2, side3 = map(float, triangle_parameters[1:])
        except ValueError:
            return False, "Sides parameters should be float."
        if validate_parameters(side1, side2, side3):
            return name, side1, side2, side3
        else:
            return False, "Triangle doesn't exist."
    else:
        return False, "Enter name snd three sides, separated commas."


def continue_input():
    """Request for continuation.

    :return:(bool) True if user input "y" or "yes"
            False otherwise
    """
    next_triangle = input_text("Do you want to enter one more triangle?").lower()
    if next_triangle != "yes" and next_triangle != "y":
        return False
    return True


def print_triangles(triangle_list):
    """Sort triangles by square and return it in descending order.

    :param triangle_list: list of Triangle objects
    :return: (str)triangles names and squares in descending order
    """
    triangles.sort(key=Triangle.get_square, reverse=True)
    result = "==========Triangles list:=========="
    for tr in range(len(triangle_list)):
        result += ("\n" + str(tr + 1) +
                   ". [Triangle {}]: {} cm".format(triangles[tr].name,
                                                   triangles[tr].square))
    return result


def validate_parameters(side_1, side_2, side_3):
    """Validate sides for triangle.

    :param side_1: (float)side of triangle
    :param side_2: (float)side of triangle
    :param side_3: (float)side of triangle
    :return: (bool) - True if triangle with specified sides exist
                      False otherwise
    """
    if side_1 > 0 and side_2 > 0 and side_3 > 0 and (side_1 + side_2 > side_3) and \
            (side_1 + side_3 > side_2) and (side_3 + side_2 > side_1):
        return True
    else:
        return False


if __name__ == "__main__":
    triangles = []
    while True:
        parameters = input_parameters()
        if parameters[0]:
            triangles.append(Triangle(*parameters))
        else:
            print(parameters[1])
        if not continue_input():
            break
    print(print_triangles(triangles))
