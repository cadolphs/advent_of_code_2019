from abc import ABCMeta, abstractmethod
from enum import Enum


class Instruction(metaclass=ABCMeta):
    def __init__(self, computer, params):
        if len(params) != self.num_args():
            raise ValueError("Wrong number of arguments")

        self.computer = computer
        self.params = params

    @classmethod
    @abstractmethod
    def num_args(cls):
        pass

    @abstractmethod
    def execute(self):
        pass

    def get_param_value(self, param_idx):
        param = self.params[param_idx]
        if param.mode == ParamModes.POSITION:
            return self.computer.get(param.value)
        elif param.mode == ParamModes.IMMEDIATE:
            return param.value
        elif param.mode == ParamModes.RELATIVE:
            return self.computer.get_relative(param.value)
        else:
            raise ValueError("Invalid parameter mode")

    def put(self, addr_param_idx, val):
        param = self.params[addr_param_idx]
        if param.mode == ParamModes.POSITION:
            self.computer.put(addr=param.value, value=val)
        elif param.mode == ParamModes.RELATIVE:
            return self.computer.put_relative(offset=param.value, value=val)


class HaltInstruction(Instruction):
    def execute(self):
        self.computer.halt()

    @classmethod
    def num_args(cls):
        return 0


class DyadicOperation(Instruction):
    def execute(self):
        op1 = self.get_param_value(0)
        op2 = self.get_param_value(1)

        res = self.func(op1, op2)

        self.put(2, res)

    @abstractmethod
    def func(self, op1, op2):
        pass

    @classmethod
    def num_args(cls):
        return 3


class AddInstruction(DyadicOperation):
    def func(self, op1, op2):
        return op1 + op2


class MultInstruction(DyadicOperation):
    def func(self, op1, op2):
        return op1 * op2


class InputInstruction(Instruction):
    def execute(self):
        input_value = self.computer.read_input()
        self.put(0, input_value)

    @classmethod
    def num_args(cls):
        return 1


class OutputInstruction(Instruction):
    def execute(self):
        val = self.get_param_value(0)
        self.computer.output(val)

    @classmethod
    def num_args(cls):
        return 1


class JumpIfTrueInstruction(Instruction):
    @classmethod
    def num_args(cls):
        return 2

    def execute(self):
        if self.get_param_value(0) != 0:
            self.computer.set_instruction_pointer(self.get_param_value(1))


class JumpIfFalseInstruction(Instruction):
    @classmethod
    def num_args(cls):
        return 2

    def execute(self):
        if self.get_param_value(0) == 0:
            self.computer.set_instruction_pointer(self.get_param_value(1))


class LessThanInstruction(DyadicOperation):
    def func(self, op1, op2):
        return 1 if op1 < op2 else 0


class EqualsInstruction(DyadicOperation):
    def func(self, op1, op2):
        return 1 if op1 == op2 else 0


class ParamModes(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Param:
    def __init__(self, value, mode=ParamModes.POSITION):
        self.value = value
        if isinstance(mode, int):
            mode = ParamModes(mode)
        self.mode = mode

    def __eq__(self, o):
        return self.value == o.value and self.mode == o.mode


class AdjustRelativeBaseInstruction(Instruction):
    @classmethod
    def num_args(cls):
        return 1

    def execute(self):
        offset = self.get_param_value(0)
        self.computer.adjust_relative_base(offset)
