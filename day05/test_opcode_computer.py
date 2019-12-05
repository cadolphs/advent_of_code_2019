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
    computer = OpcodeComputer([1,0,0,0, 2,0,0,0, 99])
    computer.run()

    assert computer.memory == [4, 0, 0, 0, 2, 0, 0, 0, 99]


@pytest.mark.parametrize('input,expected', [([1,0,0,0,99], [2,0,0,0,99]),
                                            ([2,3,0,3,99], [2,3,0,6,99]),
                                            ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
                                            ([1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99])])
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
