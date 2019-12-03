from helpers import Coord
from functools import partial

from wire_reader import WireReader


def find_intersection(wire1: WireReader, wire2: WireReader, key: callable):
    common_items = wire1.points_visited.intersection(wire2.points_visited)
    try:
        common_items.remove(Coord(0, 0))
    except KeyError:
        pass

    if not common_items:
        raise IntersectionNotFoundError
    else:
        return min(common_items, key=key)


find_closest_intersection = partial(find_intersection, key=lambda x: x.manhattan)


def find_shortest_intersection(wire1: WireReader, wire2: WireReader):
    def key(x: Coord):
        return wire1.get_step_count(x) + wire2.get_step_count(x)

    best_intersection = find_intersection(wire1, wire2, key=key)
    return best_intersection, key(best_intersection)


class IntersectionNotFoundError(Exception):
    pass
