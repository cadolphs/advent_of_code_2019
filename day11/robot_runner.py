from robot import Robot
from canvas import Canvas
from opcode_computer import OpcodeComputer
from helpers import Coord


class RobotRunner:
    def __init__(self, program, start_on_white=False):
        self.computer = OpcodeComputer(program)
        self.canvas = Canvas()

        if start_on_white:
            self.canvas.draw_at(Coord(0, 0), 1)

        self.robot = Robot(computer=self.computer, canvas=self.canvas)

        self.computer.output = self.robot.read_command
        self.computer.input_src = self.robot.get_camera

    def run(self):
        self.computer.run()

    def get_panels_painted(self):
        return self.canvas.count_painted_panels()
