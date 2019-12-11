from image import Image
from terminal_plotter import TerminalPlotter
from helpers import get_data

data = get_data(day=8)

image = Image(data, shape=(25, 6))

print(f"Image checksum is {image.checksum()}")

plotter = TerminalPlotter(symbol="█", invert=True)

plotter.plot(image.render())
