from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius: int):
        self.name = 'Circle'
        self.radius = radius

    def get_area(self):
        return round(self.radius ** 2 * math.pi, 1)

    def get_perimetr(self):
        return round(self.radius * 2 * math.pi, 1)

    @staticmethod
    def check_сircle_can_exist(self, radius: int):
        if not radius > 0:
            raise ValueError(f'Incorrect value of сircle radius: it must be positive')

        if not isinstance(radius, (int, float)):
            raise ValueError(f'Incorrect type of data, сircle radius must be in INT or FLOAT')

z