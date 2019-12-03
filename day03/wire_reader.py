from helpers import Coord

OFFSETS = {'R': Coord(1, 0), 'U': Coord(0, 1), 'L': Coord(-1, 0), 'D': Coord(0, -1)}


class WireReader:

    def __init__(self, instructions):
        self._points_visited = {}
        self.steps = 0
        self.current_pos = Coord(0, 0)
        self._points_visited[self.current_pos] = 0

        self.process_wire_instructions(instructions)

    def process_wire_instructions(self, instructions):
        for instruction in instructions:
            self.process_instruction(instruction)

    def process_instruction(self, instruction):
        direction, distance = parse_instruction(instruction)
        offset = OFFSETS[direction]
        for i in range(distance):
            self.do_single_step(offset)
            self.update_step_counter()

    def do_single_step(self, offset):
        self.steps += 1
        self.current_pos += offset

    def update_step_counter(self):
        if self.current_pos not in self._points_visited:
            self._points_visited[self.current_pos] = self.steps

    @property
    def points_visited(self):
        return set(self._points_visited.keys())

    def get_step_count(self, coord):
        return self._points_visited[coord]


def parse_instruction(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction not in OFFSETS:
        raise ValueError("Invalid direction")

    return direction, distance
