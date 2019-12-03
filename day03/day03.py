from helpers import get_data
from intersection_finder import find_closest_intersection, find_shortest_intersection
from wire_reader import WireReader

lines = [line.split(',') for line in get_data(day=3).split('\n')]

wire1 = WireReader(lines[0])
wire2 = WireReader(lines[1])

smallest_intersection = find_closest_intersection(wire1, wire2)

print(f"The smallest intersection is at {smallest_intersection} with a distance of {smallest_intersection.manhattan}")

shortest_intersection, total_steps = find_shortest_intersection(wire1, wire2)

print(f"The shortest intersection is at {shortest_intersection} with a step count of {total_steps}")