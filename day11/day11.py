from helpers import get_data, Coord
from robot_runner import RobotRunner
from canvas_plotter import CanvasPlotter

program_string = get_data(day=11)
program = [int(instruction) for instruction in program_string.split(",")]

# runner = RobotRunner(program)
# runner.run()

# print(f"Number of painted panels is {runner.get_panels_painted()}")

runner = RobotRunner(program, start_on_white=True)

runner.run()
print(f"Number of panels painted this time is {runner.get_panels_painted()}")

canvas_plotter = CanvasPlotter(invert=True)

canvas_plotter.plot(runner.canvas)
