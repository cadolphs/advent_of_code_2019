from helpers import Coord
from enum import Enum, auto


class CommandMode(Enum):
    COLOR = auto()
    DIRECTION = auto()


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class Robot:
    def __init__(self, computer, canvas):
        self.computer = computer
        self.canvas = canvas

        self.pos = Coord(0, 0)
        self.facing = Coord(0, -1)

        self.command_mode = CommandMode.COLOR

    def get_camera(self):
        return self.canvas.get(self.pos)

    def read_command(self, code):
        if self.command_mode == CommandMode.COLOR:
            self.canvas.draw_at(self.pos, code)
        else:
            self.turn_and_move(code)
        self._flip_command_mode()

    def _flip_command_mode(self):
        self.command_mode = (
            CommandMode.COLOR
            if self.command_mode == CommandMode.DIRECTION
            else CommandMode.DIRECTION
        )

    def turn_and_move(self, code):
        direction = Direction(code)
        self._turn(direction)
        self._move()

    def _turn(self, direction):
        """
        left turning: (1, 0) -> (0, -1)   so matrix is 0 1
                      (0, 1) -> (1, 0)                -1 0
        right turning: (1, 0) -> (0, 1)
                       (0, 1) -> (-1, 0)"""
        sign = 1 if direction == Direction.LEFT else -1
        self.facing = Coord(self.facing.y * sign, -self.facing.x * sign)

    def _move(self):
        self.pos = self.pos + self.facing
