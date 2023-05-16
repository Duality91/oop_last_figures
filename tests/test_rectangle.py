import pytest
from src.Rectangle import Rectangle


class TestRectangle:
    @pytest.mark.parametrize('first_side, second_side, expected_perimeter, expected_area',
                             [
                                 (10, 15, 50, 150),
                                 (2, 3, 10, 6),
                                 (5, 8, 26, 40),
                             ]
                             )
    def test_rectangle_creation_positive(self, first_side, second_side, expected_perimeter, expected_area):
        rectangle = Rectangle(first_side, second_side)
        assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
        assert rectangle.get_perimetr() == expected_perimeter, 'Expected correct perimeter'
        assert rectangle.get_area() == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('first_side, second_side',
                             [
                                 (0, 10),
                                 (-2, 2),
                                 (10, 10)
                             ],
                             ids=[
                                 'one side is zero',
                                 'one side is negative',
                                 'sides of rectangle must not be equal, otherwise it is a square'
                             ])
    def test_rectangle_creation_negative(self, first_side, second_side):
        with pytest.raises(ValueError):
            Rectangle(first_side, second_side)

    def test_two_rectangle_areas_sum(self):
        expected_sum = 176
        rectangle_1 = Rectangle(10, 17)
        rectangle_2 = Rectangle(2, 3)
        assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'

    @pytest.mark.parametrize('some_other_class', [10, 'something'], ids=['integer', 'str'])
    def test_two_rectangle_areas_sum_negative(self, some_other_class):
        rectangle_1 = Rectangle(10, 14)
        with pytest.raises(ValueError):
            rectangle_1.add_area(some_other_class)