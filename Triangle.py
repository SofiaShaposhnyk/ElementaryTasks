import math


class Triangle:
    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.square = self.get_square()

    def get_square(self):
        half_per = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(half_per * (half_per - self.side1) *
                         (half_per - self.side2) * (half_per - self.side3))
