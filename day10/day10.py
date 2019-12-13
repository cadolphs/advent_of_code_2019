from asteroid_map import AsteroidMap
from helpers import get_data

map_string = get_data(day=10)

asteroid_map = AsteroidMap.from_string(map_string)

print(asteroid_map.find_best_station())
