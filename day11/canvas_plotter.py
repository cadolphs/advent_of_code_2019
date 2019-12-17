from helpers import Coord


class CanvasPlotter:
    def __init__(self, symbol="█", invert=False):
        self.symbol = symbol
        self.space = " "
        self.invert = invert

    def plot(self, canvas):
        symbols = (self.symbol, self.space)
        if self.invert:
            symbols = (symbols[1], symbols[0])

        top_left, bottom_right = canvas.get_boundaries()

        for row in range(top_left.y, bottom_right.y + 1):
            for col in range(top_left.x, bottom_right.x + 1):
                item = canvas.get(Coord(col, row))
                print(f"{symbols[item]}", end="")
            print()
