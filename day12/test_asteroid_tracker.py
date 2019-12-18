from asteroid_tracker import AsteroidTracker


def test_initialize_with_single_line():

    my_tracker = AsteroidTracker.from_string("<x=-1, y=0, z=2>")

    assert len(my_tracker.moons) == 1
