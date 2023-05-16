from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, first_side):
        if first_side <= 0:
            raise ValueError(f"Incorrect value of square side: it must be positive")
        super().__init__(first_side, first_side)
        self.name = "Square"

    def get_area(self):
        return round(self.first_side ** 2, 2)

    def get_perimetr(self):
        return self.first_side * 4

    @staticmethod
    def check_square_can_exist(first_side: int):
        if not first_side > 0:
            raise ValueError(f'Incorrect value of square side: it must be positive')

        elif first_side not in int or float:
            raise ValueError(f'Incorrect type of data, square sides must be in INT or FLOAT')



# square = Square(10) # Так создаем квадрат со стороной 10
# v = square.get_area()
#
# print(v)


