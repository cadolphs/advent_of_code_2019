from helpers import get_data
from intersection_finder import find_closest_intersection
from wire_reader import wire_instructions_to_set

lines = [line.split(',') for line in get_data(day=3).split('\n')]

points_of_wire_1 = wire_instructions_to_set(lines[0])
points_of_wire_2 = wire_instructions_to_set(lines[1])

smallest_intersection = find_closest_intersection(points_of_wire_1, points_of_wire_2)

print(f"The smallest intersection is at {smallest_intersection} with a distance of {smallest_intersection.manhattan}")
