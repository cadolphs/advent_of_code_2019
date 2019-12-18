import re
import numpy as np

EXPR = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)"
NUMBERS = re.compile(EXPR)


class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = np.zeros(3, dtype=int)

    @classmethod
    def from_string(cls, position_string):
        match = NUMBERS.match(position_string)
        if not match:
            raise ValueError(f"Cannot parse position string: {position_string}")
        (x, y, z) = match.groups(1)
        return cls(np.array([x, y, z], dtype=int))

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def get_potential_energy(self):
        return np.sum(np.abs(self.pos))

    def get_kinetic_energy(self):
        return np.sum(np.abs(self.vel))
