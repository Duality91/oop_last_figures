from src.Figure import Figure
import math


class Rectangle(Figure):
    def __init__(self, first_side: int, second_side: int):
        self.name = 'Rectangle'
        self.first_side = first_side
        self.second_side = second_side

    def get_area(self):
        return round(self.first_side * self.second_side, 2)

    def get_perimetr(self):
        return (self.first_side + self.second_side) * 2

    @staticmethod
    def check_rectangle_can_exist(first_side: int, second_side: int, third_side: int):
        if not (first_side > 0 or second_side > 0):
            raise ValueError(f'Incorrect value of rectangle side: it must be positive')

        elif (first_side not in int or float) or (second_side not in int or float):
            raise ValueError(f'Incorrect type of data, rectangle sides must be in INT or FLOAT')

        elif first_side != second_side:
            raise ValueError(f'Sides of rectangle must not be equal, otherwise it is a square')


