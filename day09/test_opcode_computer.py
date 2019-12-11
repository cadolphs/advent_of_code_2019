import pytest
from unittest.mock import Mock

from opcode_computer import OpcodeComputer


def test_stopping_immediately_changes_nothing():
    computer = OpcodeComputer([99, 1, 2, 3])
    computer.run()

    assert computer.memory == [99, 1, 2, 3]


def test_opcode_one_then_halting_adds_numbers():
    computer = OpcodeComputer([1, 5, 6, 7, 99, 4, 6, 0])
    computer.run()

    assert computer.memory == [1, 5, 6, 7, 99, 4, 6, 10]


def test_opcode_two_then_halting_multiplies_numbers():
    computer = OpcodeComputer([2, 5, 6, 7, 99, 4, 6, 0])
    computer.run()

    assert computer.memory == [2, 5, 6, 7, 99, 4, 6, 24]


def test_opcode_execute_second_after_first():
    computer = OpcodeComputer([1, 0, 0, 0, 2, 0, 0, 0, 99])
    computer.run()

    assert computer.memory == [4, 0, 0, 0, 2, 0, 0, 0, 99]


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_homepage_examples(input, expected):
    computer = OpcodeComputer(input)
    computer.run()

    assert computer.memory == expected


def test_read_input_asks_input_generator():
    computer = OpcodeComputer([])

    computer.input_src = iter([0, 1, 2])
    assert computer.read_input() == 0
    assert computer.read_input() == 1
    assert computer.read_input() == 2


def test_opcode_3_makes_read():
    input_src = iter([55])
    computer = OpcodeComputer([3, 0, 99], input_src=input_src)

    computer.run()

    assert computer.memory == [55, 0, 99]


def test_opcode_4_provides_output():
    output = Mock()
    computer = OpcodeComputer([4, 0, 99], output=output)

    computer.run()

    output.assert_called_with(4)


def test_adding_two_numbers_in_direct_mode():
    computer = OpcodeComputer([1101, 2, 3, 0, 99])
    computer.run()

    assert computer.memory == [5, 2, 3, 0, 99]


def test_immediate_mode_homepage_example():
    computer = OpcodeComputer([1002, 4, 3, 4, 33])
    computer.run()

    assert computer.memory == [1002, 4, 3, 4, 99]


@pytest.mark.parametrize("input,expected", [(8, 1), (9, 0), (7, 0)])
def test_equals_example(input, expected):
    computer = OpcodeComputer([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    computer.input_src = iter([input])
    computer.output = Mock()

    computer.run()

    computer.output.assert_called_with(expected)


@pytest.mark.parametrize("input,expected", [(8, 0), (9, 0), (7, 1)])
def test_lt_example(input, expected):
    computer = OpcodeComputer([3, 3, 1107, -1, 8, 3, 4, 3, 99])
    computer.input_src = iter([input])
    computer.output = Mock()

    computer.run()

    computer.output.assert_called_with(expected)


def test_simple_jump():
    computer = OpcodeComputer([1106, 0, 6, 104, 1, 99, 104, 2, 99])
    computer.output = Mock()
    computer.run()
    computer.output.assert_called_with(2)


@pytest.mark.parametrize("input,expected", [(8, 1), (9, 1), (0, 0)])
def test_lt_example(input, expected):
    computer = OpcodeComputer([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])
    computer.input_src = iter([input])
    computer.output = Mock()

    computer.run()

    computer.output.assert_called_with(expected)


@pytest.mark.parametrize("input,expected", [(8, 1000), (9, 1001), (6, 999)])
def test_large_example(input, expected):
    computer = OpcodeComputer(
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ]
    )

    computer.input_src = iter([input])
    computer.output = Mock()

    computer.run()

    computer.output.assert_called_with(expected)


def test_can_read_from_beyond_memory():
    # Output from address 15, which is initially empty
    output = Mock()
    computer = OpcodeComputer(program=[4, 15, 99], output=output)

    computer.run()

    output.assert_called_with(0)


def test_negative_read_test():
    output_list = []
    output = lambda x: output_list.append(x)
    program = list(
        map(int, "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(","))
    )
    computer = OpcodeComputer(program, output=output)
    computer.run()

    assert output_list == program


def test_big_number_output():
    output_list = []
    output = lambda x: output_list.append(x)

    program = list(map(int, "1102,34915192,34915192,7,4,7,99,0".split(",")))

    computer = OpcodeComputer(program, output=output)
    computer.run()

    assert len(str(output_list[-1])) == 16


def test_middle_output():
    output_list = []
    output = lambda x: output_list.append(x)
    program = list(map(int, "104,1125899906842624,99".split(",")))

    computer = OpcodeComputer(program, output=output)
    computer.run()

    assert output_list[-1] == 1125899906842624
