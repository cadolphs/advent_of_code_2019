import pytest
from intersection_finder import find_closest_intersection, IntersectionNotFoundError
from helpers import Coord


def test_empty_sets_have_no_intersection():
    set1 = set()
    set2 = set()

    with pytest.raises(IntersectionNotFoundError):
        find_closest_intersection(set1, set2)


def test_disjoint_sets_have_no_intersection():
    set1 = set()
    set2 = set()

    set1.add(Coord(1, 2))
    set2.add(Coord(2, 3))


def test_equal_one_item_sets_intersect_at_that_item():
    set1 = set([Coord(1, 2)])
    set2 = set([Coord(1, 2)])

    assert find_closest_intersection(set1, set2) == Coord(1, 2)


def test_if_only_00_is_common_have_no_intersection():
    set1 = set([Coord(0, 0)])
    set2 = set([Coord(0, 0)])

    with pytest.raises(IntersectionNotFoundError):
        find_closest_intersection(set1, set2)


def test_actually_finds_smallest_intersection():
    set1 = set([Coord(0, 0), Coord(2, 3), Coord(1, 20), Coord(10, 0)])
    set2 = set([Coord(0, 0), Coord(2, 3), Coord(10, 0), Coord(1, 20)])

    assert find_closest_intersection(set1, set2) == Coord(2, 3)
