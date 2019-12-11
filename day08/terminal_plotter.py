class TerminalPlotter:
    def __init__(self, symbol="█", invert=False):
        self.symbol = symbol
        self.space = " "
        self.invert = invert

    def plot(self, image_data):
        symbols = (self.symbol, self.space)
        if self.invert:
            symbols = (symbols[1], symbols[0])

        def print_row(row):
            for item in row:
                print(f"{symbols[item]}", end="")

        for row in image_data:
            print_row(row)
            print()
