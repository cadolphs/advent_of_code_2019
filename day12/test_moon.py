from moon import Moon
import numpy as np


def test_moon_position_parsing():
    moon = Moon.from_string("<x=-1, y=0, z=2>")
    assert np.all(moon.pos == np.array([-1, 0, 2]))
