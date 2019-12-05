from instruction import HaltInstruction, AddInstruction, MultInstruction, InputInstruction
from unittest.mock import Mock
import pytest


def test_halt_instruction_calls_program_halt():
    opcode_computer = Mock()
    halt_instruction = HaltInstruction(opcode_computer, ())

    halt_instruction.execute()

    assert opcode_computer.halt.called is True


@pytest.fixture
def stub_computer():
    class StubComputer:
        def get(self, addr):
            if addr == 3:
                return 42
            if addr == 5:
                return 58

        def put(self, addr, value):
            pass

        def read_input(self):
            return 66

    return StubComputer()


def test_addition_instruction_puts_sum_to_address(stub_computer):
    opcode_computer = stub_computer
    opcode_computer.put = Mock()

    addr_orig1 = 3
    addr_orig2 = 5
    addr_target = 10

    addition_instruction = AddInstruction(opcode_computer, [addr_orig1, addr_orig2, addr_target])
    addition_instruction.execute()

    opcode_computer.put.assert_called_with(10, 100)


def test_mult_instruciton_puts_difference_to_address(stub_computer):
    opcode_computer = stub_computer
    opcode_computer.put = Mock()
    addr_orig1 = 3
    addr_orig2 = 5
    addr_target = 10

    subtraction_instruction = MultInstruction(opcode_computer, [addr_orig1, addr_orig2, addr_target])
    subtraction_instruction.execute()

    opcode_computer.put.assert_called_with(10, 42 * 58)


def test_input_instruction_asks_computer_for_input():
    opcode_computer = Mock()
    opcode_computer.read_input = Mock(return_value=55)

    addr_target = 10
    input_instruction = InputInstruction(opcode_computer, [addr_target])

    input_instruction.execute()

    assert opcode_computer.read_input.called is True
    opcode_computer.put.assert_called_with(10, 55)