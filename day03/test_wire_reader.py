from wire_reader import wire_instructions_to_set


def test_empty_instructions_give_central_point():
    points_visited = wire_instructions_to_set([])
    assert points_visited == set([(0, 0)])


def test_go_one_right():
    points_visited = wire_instructions_to_set(['R1'])
    assert points_visited == set([(0, 0), (1, 0)])


def test_go_one_up():
    points_visited = wire_instructions_to_set(['U1'])
    assert points_visited == set([(0, 0), (0, 1)])


def test_go_two_right():
    points_visited = wire_instructions_to_set(['R2'])
    assert points_visited == set([(0, 0), (1, 0), (2, 0)])


def test_go_two_right_then_one_up():
    points_visited = wire_instructions_to_set(['R2', 'U1'])
    assert points_visited == set([(0, 0), (1, 0), (2, 0), (2, 1)])
