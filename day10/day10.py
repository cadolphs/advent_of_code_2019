from asteroid_map import AsteroidMap, BestStationFinder
from laser import LaserDriver, Laser
from helpers import get_data
from itertools import islice

map_string = get_data(day=10)

asteroid_map = AsteroidMap.from_string(map_string)

best_station_finder = BestStationFinder(asteroid_map)
best_station, best_amount = best_station_finder.find_best_station()
print(f"Best station can see {best_amount} asteroids.")

laser_driver = LaserDriver(Laser(asteroid_map, best_station))

asteroids_hit = [asteroid for asteroid in islice(laser_driver.fire_and_forget(), 200)]

print(f"The 200th asteroid hit was at position {asteroids_hit[-1]}")
print(f"Its code is {asteroids_hit[-1].x * 100 + asteroids_hit[-1].y}")
