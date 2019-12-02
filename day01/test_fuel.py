import pytest

from fuel import compute_fuel, compute_fuel_total, total_fuel_per_module


def test_empty_list_uses_no_fuel():
    assert compute_fuel([]) == 0


def test_item_divisible_by_three_gives_correct_answer():
    assert compute_fuel([12]) == 2


def test_item_not_divisible_by_three_gives_correct_answer():
    assert compute_fuel([14]) == 2


def test_works_for_list_of_items():
    assert compute_fuel([12, 14]) == 4


@pytest.mark.parametrize('weight, expected_fuel', [(0, 0),
                                                   (14, 2),
                                                   (1969, 966)])
def test_total_fuel_per_module(weight, expected_fuel):
    assert total_fuel_per_module(weight) == expected_fuel
