from instruction import HaltInstruction, AddInstruction, MultInstruction, InputInstruction, OutputInstruction, Param
from instruction import JumpIfTrueInstruction, JumpIfFalseInstruction, LessThanInstruction, EqualsInstruction
from collections import defaultdict

OPCODE_TYPES = {99: HaltInstruction,
                1: AddInstruction,
                2: MultInstruction,
                3: InputInstruction,
                4: OutputInstruction,
                5: JumpIfTrueInstruction,
                6: JumpIfFalseInstruction,
                7: LessThanInstruction,
                8: EqualsInstruction}


class InstructionFactory:
    def __init__(self, computer):
        self.computer = computer

    def load_instruction(self, pos):
        instruction = self.computer.get(pos)
        opcode = instruction % 100
        InstructionClass = OPCODE_TYPES[opcode]

        num_args = InstructionClass.num_args()

        arg_values = self.computer[pos + 1:pos + num_args + 1]

        modes = [0] * num_args
        self.set_modes(modes, instruction)

        params = [Param(value, mode) for value, mode in zip(arg_values, modes)]

        return InstructionClass(self.computer, params)

    def set_modes(self, modes, instruction):
        mode_numbers = instruction // 100
        i = 0
        while mode_numbers > 0:
            mode_numbers, modes[i] = divmod(mode_numbers, 10)
            i += 1
