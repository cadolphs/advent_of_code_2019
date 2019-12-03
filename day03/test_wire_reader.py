from wire_reader import WireReader
from helpers import Coord

### These are for the simple (part a) functionality

def test_empty_instructions_give_central_point():
    reader = WireReader([])
    reader.points_visited
    assert reader.points_visited == set([(0, 0)])


def test_go_one_right():
    reader = WireReader(['R1'])
    assert reader.points_visited == set([(0, 0), (1, 0)])


def test_go_one_up():
    reader = WireReader(['U1'])
    assert reader.points_visited == set([(0, 0), (0, 1)])


def test_go_two_right():
    reader = WireReader(['R2'])
    assert reader.points_visited == set([(0, 0), (1, 0), (2, 0)])


def test_go_two_right_then_one_up():
    reader = WireReader(['R2', 'U1'])
    assert reader.points_visited == set([(0, 0), (1, 0), (2, 0), (2, 1)])

### These are for the more complex (part b) functionality


def test_first_visited_coord_has_count_1():
    reader = WireReader(['R1'])
    assert reader.get_step_count(Coord(1, 0)) == 1


def test_visiting_again_doesnt_update():
    reader = WireReader(['R2', 'L3'])
    assert reader.get_step_count(Coord(0, 0)) == 0
    assert reader.get_step_count(Coord(1, 0)) == 1
    assert reader.get_step_count(Coord(2, 0)) == 2
    assert reader.get_step_count(Coord(-1, 0)) == 5