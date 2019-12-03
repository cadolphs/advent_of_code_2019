OFFSETS = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}


def wire_instructions_to_set(instructions):
    current_pos = (0, 0)
    points_visited = set([current_pos])
    for instruction in instructions:
        direction, distance = parse_instruction(instruction)
        offset = OFFSETS[direction]

        points_visited.update(tuple_add(current_pos, tuple_times(offset, i)) for i in range(1, distance + 1))
        current_pos = tuple_add(current_pos, tuple_times(offset, distance))

    return points_visited


def parse_instruction(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction not in OFFSETS:
        raise ValueError("Invalid direction")

    return direction, distance


def tuple_times(tup, factor):
    return tuple(i * factor for i in tup)


def tuple_add(tup1, tup2):
    return tuple(i + j for i, j in zip(tup1, tup2))
