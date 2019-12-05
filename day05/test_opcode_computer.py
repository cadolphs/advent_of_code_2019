import pytest

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