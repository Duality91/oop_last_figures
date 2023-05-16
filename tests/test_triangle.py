import pytest
from src.Triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize('first_side, second_side, third_side, expected_perimeter, expected_area',
                             [
                                 (10, 10, 10, 30, 43.3),
                                 (2, 2, 3, 7, 1.98),
                                 (5, 6, 8, 19, 14.98),
                             ]
                             )
    def test_triangle_creation_positive(self, first_side, second_side, third_side, expected_perimeter, expected_area):
        triangle = Triangle(first_side, second_side, third_side)
        assert triangle.name == 'Triangle', 'Expected name is Triangle'
        assert triangle.get_perimetr() == expected_perimeter, 'Expected correct perimeter'
        assert triangle.get_area() == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('first_side, second_side, third_side',
                             [
                                 (0, 10, 10),
                                 (-2, 2, 3),
                                 (10, 10, 30),
                             ],
                             ids=[
                                 'one side is zero',
                                 'one side is negative',
                                 'can not create rectangle with these sides'
                             ])
    def test_triangle_creation_negative(self, first_side, second_side, third_side):
        with pytest.raises(ValueError):
            Triangle(first_side, second_side, third_side)

    def test_two_triangle_areas_sum(self):
        expected_sum = 45.28
        triangle_1 = Triangle(10, 10, 10)
        triangle_2 = Triangle(2, 2, 3)
        assert triangle_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'

    @pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
    def test_two_triangle_areas_sum_negative(self, some_other_class):
        triangle_1 = Triangle(10, 10, 10)
        with pytest.raises(ValueError):
            triangle_1.add_area(some_other_class)