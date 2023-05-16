import pytest
from src.Square import Square


class TestSquare:
    @pytest.mark.parametrize('first_side, expected_perimeter, expected_area',
                             [
                                 (10, 40, 100),
                                 (2, 8, 4),
                                 (5, 20, 25),
                             ]
                             )
    def test_square_creation_positive(self, first_side, expected_perimeter, expected_area):
        square = Square(first_side)
        assert square.name == 'Square', 'Expected name is Square'
        assert square.get_perimetr() == expected_perimeter, 'Expected correct perimeter'
        assert square.get_area() == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('first_side',
                             [
                                 (0), (-2)
                             ],
                             ids=[
                                 'one side is zero',
                                 'one side is negative'
                             ])
    def test_square_creation_negative(self, first_side):
        with pytest.raises(ValueError):
            Square(first_side)

    def test_two_square_areas_sum(self):
        expected_sum = 164
        rectangle_1 = Square(10)
        rectangle_2 = Square(8)
        assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'

    @pytest.mark.parametrize('some_other_class', ['something'], ids=['str'])
    def test_two_square_areas_sum_negative(self, some_other_class):
        rectangle_1 = Square(10)
        with pytest.raises(ValueError):
            rectangle_1.add_area(some_other_class)