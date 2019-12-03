from dataclasses import dataclass


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, o):
        return Coord(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Coord(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        if not isinstance(o, int):
            raise TypeError("So far, we can only multiply coords with ints")
        return Coord(self.x * o, self.y * o)

    def __eq__(self, o):
        if isinstance(o, Coord):
            return (self.x, self.y) == (o.x, o.y)
        elif isinstance(o, tuple):
            return self.x == o[0] and self.y == o[1]
