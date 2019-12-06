from orbit_map import OrbitMap


def test_adding_single_orbit_adds_nodes():
    orbit_map = OrbitMap()
    orbit_map.add_orbit('A', 'B')

    assert 'A' in orbit_map.nodes()
    assert 'B' in orbit_map.nodes()


def test_single_orbit_gives_count_one():
    orbit_map = OrbitMap(source='A')
    orbit_map.add_orbit('A', 'B')

    assert orbit_map.count_orbits('B') == 1


def test_indirect_orbits_get_added():
    orbit_map = OrbitMap()
    orbit_map.add_orbit('COM', 'B')
    orbit_map.add_orbit('B', 'C')

    assert orbit_map.count_orbits('C') == 2


def test_orbit_from_string():
    orbit_map = OrbitMap.from_string("COM)B\nB)C\nC)D")

    assert set(orbit_map.nodes()) == {"COM", "B", "C", "D"}


def test_find_orbitee():
    orbit_map = OrbitMap.from_string("COM)B\nB)C\nC)D")

    orbitee_of_C = orbit_map.get_orbitee('C')
    assert orbitee_of_C == 'B'


def test_find_path_between():
    orbit_map = OrbitMap.from_string("COM)B\nB)C\nC)D")

    path = orbit_map.find_path_between('D', 'B')
    assert len(path) == 3


def test_find_num_transfers():
    orbit_map = OrbitMap.from_string('COM)B\nCOM)XX\nB)C\nC)D')

    num_transfers = orbit_map.find_number_of_transfers('D', 'XX')
    # D is orbiting C, XX is orbiting DOM, so transfers = from C to B to COM
    assert num_transfers == 2