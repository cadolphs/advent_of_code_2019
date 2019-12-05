from instruction import HaltInstruction, AddInstruction, MultInstruction
from unittest.mock import Mock
import pytest


def test_halt_instruction_calls_program_halt():
    opcode_computer = Mock()
    halt_instruction = HaltInstruction(opcode_computer)

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

    return StubComputer()


def test_addition_instruction_puts_sum_to_address(stub_computer):
    opcode_computer = stub_computer
    opcode_computer.put = Mock()

    addr_orig1 = 3
    addr_orig2 = 5
    addr_target = 10

    addition_instruction = AddInstruction(opcode_computer, addr_orig1, addr_orig2, addr_target)
    addition_instruction.execute()

    opcode_computer.put.assert_called_with(10, 100)


def test_mult_instruciton_puts_difference_to_address(stub_computer):
    opcode_computer = stub_computer
    opcode_computer.put = Mock()
    addr_orig1 = 3
    addr_orig2 = 5
    addr_target = 10

    subtraction_instruction = MultInstruction(opcode_computer, addr_orig1, addr_orig2, addr_target)
    subtraction_instruction.execute()

    opcode_computer.put.assert_called_with(10, 42 * 58)