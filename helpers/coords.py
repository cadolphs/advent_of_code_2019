from dataclasses import dataclass
from math import gcd, sqrt, atan2, pi


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    @property
    def norm2(self):
        return sqrt(self.x ** 2 + self.y ** 2)

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

    def angle_with(self, o):
        """Return angle, in interval 0, 2pi, between this coord and the other coord"""
        # A bit hacky but this should work:
        vec_a = (self.x / self.norm2, self.y / self.norm2)
        vec_b = (o.x / o.norm2, o.y / o.norm2)

        signed_angle = atan2(
            vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0],
            vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1],
        )
        if signed_angle < 0:
            signed_angle += 2 * pi
        return signed_angle
