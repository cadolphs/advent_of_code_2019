import pytest
from intersection_finder import find_closest_intersection, IntersectionNotFoundError, find_shortest_intersection
from helpers import Coord
from wire_reader import WireReader


class WireStub:
    def __init__(self, points):
        self.points_visited = points


def test_empty_sets_have_no_intersection():
    wire1 = WireStub(set())
    wire2 = WireStub(set())

    with pytest.raises(IntersectionNotFoundError):
        find_closest_intersection(wire1, wire2)


def test_disjoint_sets_have_no_intersection():
    wire1 = WireStub(set())
    wire2 = WireStub(set())

    wire1.points_visited.add(Coord(1, 2))
    wire2.points_visited.add(Coord(2, 3))

    with pytest.raises(IntersectionNotFoundError):
        find_closest_intersection(wire1, wire2)


def test_equal_one_item_sets_intersect_at_that_item():
    wire1 = WireStub(set([Coord(1, 2)]))
    wire2 = WireStub(set([Coord(1, 2)]))

    assert find_closest_intersection(wire1, wire2) == Coord(1, 2)


def test_if_only_00_is_common_have_no_intersection():
    wire1 = WireStub(set([Coord(0, 0)]))
    wire2 = WireStub(set([Coord(0, 0)]))

    with pytest.raises(IntersectionNotFoundError):
        find_closest_intersection(wire1, wire2)


def test_actually_finds_smallest_intersection():
    wire1 = WireStub(set([Coord(0, 0), Coord(2, 3), Coord(1, 20), Coord(10, 0)]))
    wire2 = WireStub(set([Coord(0, 0), Coord(2, 3), Coord(10, 0), Coord(1, 20)]))

    assert find_closest_intersection(wire1, wire2) == Coord(2, 3)


# Once the individual steps are in place this is quite easy, so just do a big "integration" test
def test_examples_of_shortest_intersection():
    wire1 = WireReader("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','))
    wire2 = WireReader("U62,R66,U55,R34,D71,R55,D58,R83".split(','))

    assert find_shortest_intersection(wire1, wire2)[1] == 610

    wire1 = WireReader("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(','))
    wire2 = WireReader("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(','))

    assert find_shortest_intersection(wire1, wire2)[1] == 410
