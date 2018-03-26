import re
from Triangle import Triangle


def input_parameters():
    print("Input triangle parameters:")
    triangle_parameters = re.sub("[ /t]", "", input()).lower().split(",")
    if len(triangle_parameters) == 4:
        name = triangle_parameters[0]
        try:
            side1, side2, side3 = map(float, triangle_parameters[1:])
        except ValueError:
            print("Sides parameters should be float.")
            return False
        if validate_parameters(side1, side2, side3):
            return name, side1, side2, side3
        else:
            print("Triangle doesn't exist.")
            return False
    else:
        print("Enter name snd three sides, separated commas.")
        return False


def continue_input():
    print("Do you want to enter one more triangle?")
    next_triangle = input().lower()
    if next_triangle != "yes" and next_triangle != "y":
        return False
    return True


def print_triangles(triangle_list):
    print("==========Triangles list:==========")
    for tr in range(len(triangle_list)):
        print((tr + 1), ". [Triangle {}]: {:.2f} cm".format(triangles[tr].name, triangles[tr].square))


def validate_parameters(side_1, side_2, side_3):
    if side_1 > 0 and side_2 > 0 and side_3 > 0 and (side_1 + side_2 > side_3) and \
            (side_1 + side_3 > side_2) and (side_3 + side_2 > side_3):
        return True
    else:
        return False


if __name__ == "__main__":
    triangles = []
    while True:
        parameters = input_parameters()
        if parameters:
            triangles.append(Triangle(*parameters))
        if not continue_input():
            break
    triangles.sort(key=Triangle.get_square, reverse=True)
    print_triangles(triangles)
