def can_we_fit(envelop1, envelop2):
    envelop1, envelop2 = sort_envelops(envelop1, envelop2)
    if (is_sqrt_sides_bigger(envelop1, envelop2) and
        is_sum_sides_bigger(envelop1, envelop2) and
            is_min_side_bigger(envelop1, envelop2)):
        return print("Possible!")
    else:
        return print("Impossible!")


def is_sqrt_sides_bigger(envelop1, envelop2):
    if envelop1["side1"]**2 + envelop1["side2"]**2 > envelop2["side1"]**2 + envelop2["side2"]:
        return True
    else:
        return False


def is_sum_sides_bigger(envelop1, envelop2):
    if envelop1["side1"] + envelop1["side2"] > envelop2['side1'] + envelop2["side2"]:
        return True
    else:
        return False


def is_min_side_bigger(envelop1, envelop2):
    if min(envelop1["side1"], envelop1["side2"]) > min(envelop2["side1"], envelop2["side2"]):
        return True
    else:
        return False


def sort_envelops(envelop1, envelop2):
    if envelop1["side1"] * envelop1["side2"] < envelop2["side1"] * envelop2["side2"]:
        return envelop2, envelop1
    else:
        return envelop1, envelop2


def validate_side(side):
    success = False
    while not success:
        try:
            side = float(side)
            success = True
        except ValueError:
            print("Wrong! Parameter should be float.\nTry again:")
            side = input()
            continue
        if side <= 0:
            print("Wrong! Parameters should be bigger then 0.\nTry again:")
            side = input()
            success = False
    return side


def input_parameters():
    print("Enter first envelop parameters:")
    side_1 = validate_side(input("Side 1:"))
    side_2 = validate_side(input("Side 2:"))
    envelop1 = {"side1": side_1, "side2": side_2}
    print("Enter second envelop parameters:")
    side_1 = validate_side(input("Side 1:"))
    side_2 = validate_side(input("Side 2:"))
    envelop2 = {"side1": side_1, "side2": side_2}
    return envelop1, envelop2


if __name__ == "__main__":
    one_more = True
    while one_more:
        first_envelop, second_envelop = input_parameters()
        if first_envelop:
            can_we_fit(first_envelop, second_envelop)
            print("Do you want to continue?")
            answer = input().lower()
            if answer != "yes" and answer != "y":
                one_more = False
