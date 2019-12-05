from instruction_factory import InstructionFactory


class OpcodeComputer:
    '''Class representing our Integer Computer'''

    def __init__(self, program, input_src=None, output=None):
        '''Initialize with program, given as a list of integers'''
        self.memory = program
        self.instruction_pointer = 0
        self.instruction_factory = InstructionFactory(self)
        self.input_src = input_src
        self.output = output

    def set_inputs(self, noun, verb):
        '''Provide inputs in the form of a (noun, verb) tuple.

        Inputs are written into memory positions 1 and 2
        '''
        self.memory[1], self.memory[2] = noun, verb

    def run(self):
        '''Execute the program currently in the memory, until a 99 opcode is encountered.
        
        Note: As time goes on and more instructiosn get added, we would probably refactor this. Create 
        a class for the various instructions and have them be responsible for computing the correct results.
        
        The "switch" statement for the opcodes would be put into a factory class / factory method that creates 
        instruction objects.'''
        
        while True:
            # Note: Right now we don't have to worry about endless loops, because the current program
            # doesn't jump around.
            instruction = self.instruction_factory.load_instruction(self.instruction_pointer)
            try:
                instruction.execute()
            except ProgramTerminatedException as e:
                print(f"Program terminated with opcode {e.args[0]}")
                return
    
            self.instruction_pointer += 1 + instruction.num_args()

    def halt(self):
        raise ProgramTerminatedException(0)

    def __getitem__(self, key):
        return self.memory[key]

    def get(self, addr):
        return self.memory[addr]

    def put(self, addr, value):
        self.memory[addr] = value

    def read_input(self):
        return next(self.input_src)


class ProgramTerminatedException(Exception):
    pass
