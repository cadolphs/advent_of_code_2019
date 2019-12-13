from laser import Laser
from unittest.mock import Mock, MagicMock
from helpers import Coord
from asteroid_map import AsteroidMap


def test_firing_laser_removes_hit_asteroid():
    asteroid_map = MagicMock()
    laser_position = Coord(3, 4)

    asteroid_map.all_asteroids_in_line_of = MagicMock(
        return_value=iter([Coord(42, 55)])
    )

    laser = Laser(asteroid_map, laser_position)

    laser.fire()

    asteroid_map.remove_asteroid.assert_called_with(Coord(42, 55))


def test_rotating_to_next_asteroid():
    ## Laser map:
    ## #.
    ## X#
    asteroid_map = AsteroidMap.from_string("##\n##")
    laser_position = Coord(0, 1)

    laser = Laser(asteroid_map, laser_position)

    laser.fire()
    laser.rotate_to_next_asteroid()

    assert laser.laser_direction == Coord(1, -1)

