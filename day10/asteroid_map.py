from helpers import Coord


class AsteroidMap:
    def __init__(self, shape, asteroid_positions):
        self.shape = shape
        self.asteroid_positions = asteroid_positions

    def all_asteroids_in_line_of(self, start, direction):
        pos_to_check = start + direction

        while self._is_valid_pos(pos_to_check):
            if pos_to_check in self.asteroid_positions:
                yield pos_to_check
            pos_to_check = pos_to_check + direction

    def _is_valid_pos(self, pos):
        valid = (0 <= pos.x < self.shape[0]) and (0 <= pos.y < self.shape[1])
        return valid

    @classmethod
    def from_string(cls, map_string):
        rows = map_string.split("\n")

        asteroids = set()

        for row_pos, row in enumerate(rows):

            for col_pos, symbol in enumerate(row):
                if symbol == "#":
                    asteroids.add(Coord(col_pos, row_pos))
                elif symbol != ".":
                    raise ValueError("Invalid symbol in input")

        num_cols = len(rows[0])
        shape = (num_cols, len(rows))
        return cls(shape, asteroids)


class BestStationFinder:
    def __init__(self, asteroid_map):
        self.asteroid_map = asteroid_map
        self._initialize_seen_by_dict()

    def _initialize_seen_by_dict(self):
        self._seen_by = {
            asteroid: set(self.asteroid_map.asteroid_positions)
            for asteroid in self.asteroid_map.asteroid_positions
        }

        for asteroid, seen_set in self._seen_by.items():
            seen_set.remove(asteroid)

    def find_best_station(self):

        for asteroid in self.asteroid_map.asteroid_positions:
            self._remove_asteroids_not_seen_from(asteroid)

        best_station = max(
            self.asteroid_map.asteroid_positions, key=lambda x: len(self._seen_by[x])
        )

        return best_station, len(self._seen_by[best_station])

    def _remove_asteroids_not_seen_from(self, asteroid):
        asteroids_to_try = sorted(
            set(self._seen_by[asteroid]), key=lambda x: (x - asteroid).manhattan
        )
        for other_asteroid in asteroids_to_try:
            if other_asteroid in self._seen_by[asteroid]:
                self._remove_asteroids_in_line_of(asteroid, other_asteroid)

    def _remove_asteroids_in_line_of(self, asteroid, other_asteroid):
        distance = other_asteroid - asteroid
        step = distance.normalized()

        for hidden_asteroid in self.asteroid_map.all_asteroids_in_line_of(
            other_asteroid, step
        ):
            self._remove_seen(asteroid, hidden_asteroid)
            self._remove_seen(hidden_asteroid, asteroid)

    def _remove_seen(self, a, b):
        try:
            self._seen_by[a].remove(b)
        except KeyError:
            pass

