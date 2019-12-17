from robot import Robot
from unittest.mock import Mock, MagicMock
from helpers import Coord


def test_robot_passes_canvas_color_to_computer_input():
    canvas = MagicMock()
    computer = MagicMock()

    robot = Robot(computer, canvas)

    computer.input_src = robot.get_camera
    computer.read_input = Mock(side_effect=computer.input_src())

    computer.read_input()

    canvas.get.assert_called_once_with(Coord(0, 0))


def test_robot_receives_draw_input_and_updates_canvas():
    canvas = MagicMock()
    computer = MagicMock()

    robot = Robot(computer, canvas)

    robot.read_command(42)

    canvas.draw_at.assert_called_once_with(Coord(0, 0), 42)


def test_robot_receives_draw_then_turn_input_and_turns_and_moves_accordingly():
    canvas = MagicMock()
    computer = MagicMock()

    robot = Robot(computer, canvas)

    robot.read_command(42)
    robot.read_command(1)

    canvas.draw_at.assert_called_once_with(Coord(0, 0), 42)
    canvas.draw_at.reset_mock()
    assert robot.pos == Coord(1, 0)

    # Now might as well turn again a bit
    robot.read_command(55)
    robot.read_command(0)

    canvas.draw_at.assert_called_once_with(Coord(1, 0), 55)
    assert robot.pos == Coord(1, -1)
