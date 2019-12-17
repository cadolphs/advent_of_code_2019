from instruction_factory import InstructionFactory
from collections import defaultdict
from itertools import islice
from internal_memory import InternalMemory


class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(self, program, input_src=None, output=None):
        """Initialize with program, given as a list of integers"""
        self.memory = InternalMemory()
        self.load_program(program)
        self.instruction_pointer = 0
        self.instruction_factory = InstructionFactory(self)
        self.input_src = input_src
        self.output = output
        self._jumped = False
        self.relative_base = 0

    def load_program(self, program):
        for i, instr in enumerate(program):
            self.memory[i] = instr

    def set_inputs(self, noun, verb):
        """Provide inputs in the form of a (noun, verb) tuple.

        Inputs are written into memory positions 1 and 2
        """
        self.memory[1], self.memory[2] = noun, verb

    def run(self):
        """Execute the program currently in the memory, until we halt."""

        while True:
            instruction = self.instruction_factory.load_instruction(
                self.instruction_pointer
            )
            try:
                instruction.execute()
            except ProgramTerminatedException as e:
                print(f"Program terminated with opcode {e.args[0]}")
                return

            self.update_instruction_pointer(instruction.num_args())

    def set_instruction_pointer(self, new_ptr):
        self._jumped = True
        self.instruction_pointer = new_ptr

    def update_instruction_pointer(self, num_args):
        if self._jumped:
            self._jumped = False
            return

        self.instruction_pointer += num_args + 1

    def adjust_relative_base(self, offset):
        self.relative_base += offset

    def halt(self):
        raise ProgramTerminatedException(0)

    def __getitem__(self, key):
        return self.memory[key]

    def get(self, addr):
        return self.memory[addr]

    def get_relative(self, offset):
        return self.memory[self.relative_base + offset]

    def put(self, addr, value):
        self.memory[addr] = value

    def put_relative(self, offset, value):
        self.memory[offset + self.relative_base] = value

    def read_input(self):
        return self.input_src()


class ProgramTerminatedException(Exception):
    pass
