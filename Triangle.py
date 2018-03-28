import math


class Triangle:
    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.sides = (side1, side2, side3)

    def get_square(self):
        half_per = sum(self.sides) / 2
        return round(math.sqrt(half_per * (half_per - self.sides[0]) *
                         (half_per - self.sides[1]) * (half_per - self.sides[2])), 2)
