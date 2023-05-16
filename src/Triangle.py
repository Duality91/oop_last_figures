from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, first_side: int, second_side: int, third_side: int):
        self.name = 'Triangle'
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_area(self):
        half_perimetr = (self.first_side + self.second_side + self.third_side) / 2
        triangle_area = math.sqrt(half_perimetr * (half_perimetr - self.first_side) * (half_perimetr - self.second_side) * (half_perimetr - self.third_side))
        return round(triangle_area, 2)

    def get_perimetr(self):
        return self.first_side + self.second_side + self.third_side

    @staticmethod
    def check_triangle_can_exist(first_side: int, second_side: int, third_side: int):
        if not (first_side > 0 or second_side > 0 or third_side > 0):
            raise ValueError(f'Incorrect value of triangle side: it must be positive')

        elif (first_side not in int or float) or (second_side not in int or float) or (third_side not in int or float):
            raise ValueError(f'Incorrect type of data, triangle sides must be in INT or FLOAT')

        elif (first_side + second_side < third_side) or (first_side + third_side < second_side) or (second_side + third_side < first_side):
            raise ValueError("Incorrect parameters of the sides, sum of any 2 sides should be more than the third side")



