from canvas import Canvas
from helpers import Coord


def test_empty_canvas_is_zero_everywhere():
    canvas = Canvas()

    assert canvas.get(Coord(0, 0)) == 0
    assert canvas.get(Coord(42, 55)) == 0


def test_if_we_draw_somewhere_it_will_be_that_color():
    canvas = Canvas()

    canvas.draw_at(Coord(42, 55), 1)

    assert canvas.get(Coord(42, 55)) == 1


def test_correctly_count_painted_panels():
    canvas = Canvas()

    canvas.draw_at(Coord(42, 55), 1)
    canvas.draw_at(Coord(42, 55), 0)
    canvas.draw_at(Coord(1, 2), 1)

    assert canvas.count_painted_panels() == 2
