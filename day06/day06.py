from orbit_map import OrbitMap
from helpers import get_data

data = get_data(day=6)
print(data)
orbit_map = OrbitMap.from_string(data)

print(f"Total number of orbits, direct and indirect, is {orbit_map.get_total_orbit_count()}")

num_transfers = orbit_map.find_number_of_transfers('YOU', 'SAN')

print(f"To reach Santa, require a minimum of {num_transfers} orbital transfers")