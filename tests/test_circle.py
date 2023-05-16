import pytest
from src.Circle import Circle


class TestCircle:
    @pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                             [
                                 (5, 31.4, 78.5),
                                 (2, 12.6, 12.6),
                                 (40, 251.3, 5026.5),
                             ]
                             )
    def test_circle_creation_positive(self, radius, expected_perimeter, expected_area):
        circle = Circle(radius)
        assert circle.name == 'Circle', 'Expected name is Circle'
        assert circle.get_perimetr() == expected_perimeter, 'Expected correct perimeter'
        assert circle.get_area() == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('radius',
                             [(0), (-2)],
                             ids=['one side is zero',
                                 'one side is negative'])
    def test_circle_creation_negative(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    def test_two_circle_areas_sum(self):
        expected_sum = 326.8
        circle_1 = Circle(10)
        circle_2 = Circle(2)
        assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'

    @pytest.mark.parametrize('some_other_class', ['something'], ids=['str'])
    def test_two_circle_areas_sum_negative(self, some_other_class):
        circle_1 = Circle(10)
        with pytest.raises(ValueError):
            circle_1.add_area(some_other_class)