from helpers import Coord

OFFSETS = {'R': Coord(1, 0), 'U': Coord(0, 1), 'L': Coord(-1, 0), 'D': Coord(0, -1)}


def wire_instructions_to_set(instructions):
    current_pos = Coord(0, 0)
    points_visited = set([current_pos])
    for instruction in instructions:
        direction, distance = parse_instruction(instruction)
        offset = OFFSETS[direction]

        points_visited.update(current_pos + offset * i for i in range(1, distance + 1))
        current_pos = current_pos + offset * distance

    return points_visited


def parse_instruction(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction not in OFFSETS:
        raise ValueError("Invalid direction")

    return direction, distance