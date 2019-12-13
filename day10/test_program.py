# These are supposed to be end-to-end acceptance tests.

# Program needs to read in an asteroid map, then compute the
# number of asteroids in line of sight of each asteroid, and
# return the maximum to the user.

# First piece of functionality: Read in the asteroids.
from helpers import Coord
from asteroid_map import AsteroidMap, BestStationFinder
from laser import Laser
import pytest


def case2():
    map_2 = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####"
    best_2 = (Coord(5, 8), 33)

    return map_2, best_2


def case3():
    map_3 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""
    best_3 = (Coord(1, 2), 35)

    return map_3, best_3


def case4():
    map_4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
    best_4 = (Coord(11, 13), 210)

    return map_4, best_4


def test_simple_collision():
    map_string = "#..#..#"
    asteroid_map = AsteroidMap.from_string(map_string)
    best_station_finder = BestStationFinder(asteroid_map)
    best_station_finder._remove_asteroids_not_seen_from(Coord(0, 0))

    assert best_station_finder._seen_by[Coord(0, 0)] == set([Coord(3, 0)])


def test_more_granular():
    map_string, expected = case3()
    asteroid_map = AsteroidMap.from_string(map_string)
    best_station_finder = BestStationFinder(asteroid_map)

    best_station_finder._remove_asteroids_in_line_of(Coord(7, 3), Coord(7, 5))
    assert Coord(7, 6) not in best_station_finder._seen_by[Coord(7, 3)]


@pytest.mark.parametrize("case", [case2, case3, case4])
def test_end_to_end(case):
    map_string, expected = case()
    asteroid_map = AsteroidMap.from_string(map_string)
    best_station_finder = BestStationFinder(asteroid_map)

    assert best_station_finder.find_best_station() == expected


def laser_test():
    map_string = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
"""
    laser_pos = Coord(8, 3)

    return AsteroidMap.from_string(map_string), laser_pos


def test_first_thing_laser_shoots_is_correct():
    amap, laser_pos = laser_test()

    laser = Laser(amap, laser_pos)

    asteroid_hit = laser.fire()

    assert asteroid_hit == Coord(8, 1)


def test_laser_rotates_to_hit_next_thing():
    amap, laser_pos = laser_test()

    laser = Laser(amap, laser_pos)

    asteroid_hit = laser.fire()
    laser.rotate_to_next_asteroid()
    asteroid_hit = laser.fire()
    laser.rotate_to_next_asteroid()

    assert asteroid_hit == Coord(9, 0)

    asteroid_hit = laser.fire()

    assert asteroid_hit == Coord(9, 1)
