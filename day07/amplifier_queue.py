from opcode_computer import OpcodeComputer
from functools import partial

class AmplifierQueue:

    def __init__(self, program, phase_settings):
        self.num_computers = len(phase_settings)

        self.input_for_computers = [0] * (self.num_computers + 1)
        self.computers = [OpcodeComputer(list(program)) for _ in range(self.num_computers)]

        def input_getter(n):
            yield phase_settings[n]
            yield self.input_for_computers[n]

        def output_setter(n, val):
            print(f"Outputting {val} as input for computer {n+1}")
            self.input_for_computers[n+1] = val

        for i in range(self.num_computers):
            self.computers[i].input_src = input_getter(i)
            self.computers[i].output = partial(output_setter, i)

    def run(self):
        for computer in self.computers:
            print(computer)
            computer.run()

    def get_output(self):
        return self.input_for_computers[-1]
