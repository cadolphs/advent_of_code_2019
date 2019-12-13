from dataclasses import dataclass
from math import gcd


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

    def __floordiv__(self, o):
        if not isinstance(o, int):
            raise TypeError("So far we can only deal with integer divisors")
        return Coord(self.x // o, self.y // o)

    def __eq__(self, o):
        if isinstance(o, Coord):
            return (self.x, self.y) == (o.x, o.y)
        elif isinstance(o, tuple):
            return self.x == o[0] and self.y == o[1]

    @classmethod
    def from_tuple(cls, xy):
        return Coord(*xy)

    def normalized(self):
        if self.x == 0 and self.y == 0:
            return Coord(0, 0)
        elif self.x == 0:
            return Coord(0, self.y // abs(self.y))
        elif self.y == 0:
            return Coord(self.x // abs(self.x), 0)

        factor = gcd(self.x, self.y)
        return self // factor
