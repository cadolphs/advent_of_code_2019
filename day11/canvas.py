from helpers import Coord
from collections import defaultdict


class Canvas:
    def __init__(self):
        self.color_values = defaultdict(int)

    def get(self, pos: Coord):
        return self.color_values[pos]

    def draw_at(self, pos: Coord, color):
        self.color_values[pos] = color

    def count_painted_panels(self):
        return len(self.color_values.keys())

    def get_boundaries(self):
        leftmost = min(coord.x for coord in self.color_values.keys())
        rightmost = max(coord.x for coord in self.color_values.keys())
        upmost = min(coord.y for coord in self.color_values.keys())
        bottommost = max(coord.y for coord in self.color_values.keys())

        return Coord(leftmost, upmost), Coord(rightmost, bottommost)
