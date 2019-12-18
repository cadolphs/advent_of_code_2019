from helpers import get_data

from asteroid_tracker import AsteroidTracker

moon_positions = get_data(day=12)

asteroid_tracker = AsteroidTracker.from_string(moon_positions)

asteroid_tracker.n_steps(1000)

print(f"The total energy after 1000 steps is {asteroid_tracker.get_total_energy()}")
