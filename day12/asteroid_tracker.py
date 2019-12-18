from moon import Moon
from itertools import combinations
import numpy as np


class AsteroidTracker:
    def __init__(self, moons):
        self.moons = moons

    @classmethod
    def from_string(cls, position_string):
        moons = [Moon.from_string(line) for line in position_string.split("\n")]
        return cls(moons)

    def get_status_report(self):
        report_lines = [moon.get_status() for moon in self.moons]
        return "\n".join(report_lines)

    def step(self):
        self.update_velocities()
        self.update_positions()

    def n_steps(self, n):
        for _ in range(n):
            self.step()

    def update_velocities(self):
        for (moon_a, moon_b) in combinations(self.moons, 2):
            self.apply_gravity(moon_a, moon_b)

    def apply_gravity(self, moon_a, moon_b):
        distance_vector = moon_b.pos - moon_a.pos
        # Vector points from b to a
        delta_v_for_a = np.sign(distance_vector)
        # If e.g. x_a > x_b then x_dist < 0, so sign is -1.
        moon_a.vel += delta_v_for_a
        moon_b.vel -= delta_v_for_a

    def update_positions(self):
        for moon in self.moons:
            moon.pos += moon.vel

    def get_total_energy(self):
        return sum(moon.get_total_energy() for moon in self.moons)
