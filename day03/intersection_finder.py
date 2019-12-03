from helpers import Coord


def find_closest_intersection(set1: set, set2: set):
    common_items = set1.intersection(set2)
    try:
        common_items.remove(Coord(0, 0))
    except KeyError:
        pass

    if not common_items:
        raise IntersectionNotFoundError
    else:
        return min(common_items, key=lambda x: x.manhattan)


class IntersectionNotFoundError(Exception):
    pass
