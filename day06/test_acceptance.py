import pytest
from orbit_map import OrbitMap


# When a user loads a map, they can query it for its nodes
# and can ask how many direct and indirect orbits a node has.

def test_query_for_orbits():
    orbit_map = OrbitMap()
    orbit_map.add_orbit('COM', 'B')
    orbit_map.add_orbit('B', 'C')

    assert orbit_map.count_orbits('C') == 2


def test_total_orbits():
    orbit_map = OrbitMap()
    orbit_map.add_orbit('COM', 'B')
    orbit_map.add_orbit('B', 'C')

    assert orbit_map.get_total_orbit_count() == 3


