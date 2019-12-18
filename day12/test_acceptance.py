from asteroid_tracker import AsteroidTracker
from status_writer import StatusWriter
import pytest

example_input_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""


def test_loading_input():
    # We create a simulator and load the input positions form a string.

    asteroid_tracker = AsteroidTracker.from_string(example_input_1)

    status_writer = StatusWriter()
    status_line = status_writer.get_status_string(asteroid_tracker.moons)

    assert (
        status_line
        == """pos=<x=-1, y=  0, z= 2>, vel=<x= 0, y= 0, z= 0>
pos=<x= 2, y=-10, z=-7>, vel=<x= 0, y= 0, z= 0>
pos=<x= 4, y= -8, z= 8>, vel=<x= 0, y= 0, z= 0>
pos=<x= 3, y=  5, z=-1>, vel=<x= 0, y= 0, z= 0>"""
    )


def test_output_after_one_step():
    asteroid_tracker = AsteroidTracker.from_string(example_input_1)

    status_writer = StatusWriter()

    asteroid_tracker.step()
    status_line = status_writer.get_status_string(asteroid_tracker.moons)
    assert (
        status_line
        == """pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>
pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>
pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>
pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>"""
    )


def test_total_energy():
    asteroid_tracker = AsteroidTracker.from_string(example_input_1)

    for _ in range(10):
        asteroid_tracker.step()

    assert asteroid_tracker.get_total_energy() == 179
