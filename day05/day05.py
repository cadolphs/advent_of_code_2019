from opcode_computer import OpcodeComputer
from helpers import get_data

data = get_data(day=5)

program_master = [int(entry) for entry in data.split(',')]

computer = OpcodeComputer(list(program_master), input_src=iter([1]), output=print)
computer.run()

# Restart computer, use 5 as input
computer = OpcodeComputer(list(program_master), input_src=iter([5]), output=print)
computer.run()