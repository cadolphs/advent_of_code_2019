from helpers import get_data
from opcode_computer import OpcodeComputer

program = list(map(int, get_data(day=9).split(",")))

computer = OpcodeComputer(program, output=print, input_src=iter([1]))

computer.run()

computer = OpcodeComputer(program, output=print, input_src=iter([2]))
computer.run()

