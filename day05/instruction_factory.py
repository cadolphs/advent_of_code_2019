from instruction import HaltInstruction, AddInstruction, MultInstruction, InputInstruction, OutputInstruction

OPCODE_TYPES = {99: HaltInstruction,
                1: AddInstruction,
                2: MultInstruction,
                3: InputInstruction,
                4: OutputInstruction}


class InstructionFactory:
    def __init__(self, computer):
        self.computer = computer

    def load_instruction(self, pos):
        opcode = self.computer.get(pos)
        InstructionClass = OPCODE_TYPES[opcode]

        num_args = InstructionClass.num_args()

        args = self.computer[pos + 1:pos + num_args + 1]

        return InstructionClass(self.computer, args)
