from opcode_computer import OpcodeComputer
from instruction import HaltInstruction, AddInstruction, MultInstruction
from instruction_factory import InstructionFactory


def test_99_makes_halt_instruction():
    computer = OpcodeComputer([99, 1, 2, 3])
    factory = InstructionFactory(computer)

    instr = factory.load_instruction(0)

    assert isinstance(instr, HaltInstruction)
    assert instr.computer == computer


def test_1_makes_add_instruction():
    computer = OpcodeComputer([1, 2, 3, 0, 99])
    factory = InstructionFactory(computer)

    instr = factory.load_instruction(0)

    assert isinstance(instr, AddInstruction)
    assert instr.addr_src_1 == 2
    assert instr.addr_src_2 == 3
    assert instr.addr_tgt == 0


def test_2_makes_mult_instruction():
    computer = OpcodeComputer([2, 2, 3, 0, 99])
    factory = InstructionFactory(computer)

    instr = factory.load_instruction(0)

    assert isinstance(instr, MultInstruction)
    assert instr.addr_src_1 == 2
    assert instr.addr_src_2 == 3
    assert instr.addr_tgt == 0