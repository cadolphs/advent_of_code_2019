from itertools import product

from opcode_computer import OpcodeComputer
from helpers import get_data

data = get_data(day=2)

program_master = [int(entry) for entry in data.split(',')]

computer = OpcodeComputer(list(program_master))
computer.set_inputs(12, 2)
computer.run()

print(f"Value left at position 0 is {computer[0]}")

for noun, verb in product(range(1, 100), repeat=2):
    computer = OpcodeComputer(list(program_master))
    computer.set_inputs(noun, verb)
    computer.run()

    if computer.output == 19690720:
        break

print(f"Correct output provided by {noun}, {verb}, with key {100*noun+verb}")