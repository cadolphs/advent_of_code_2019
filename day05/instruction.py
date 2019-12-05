from abc import ABCMeta, abstractmethod


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


class HaltInstruction(Instruction):
    def execute(self):
        self.computer.halt()

    @classmethod
    def num_args(cls):
        return 0


class DyadicOperation(Instruction):

    def execute(self):
        op1 = self.computer.get(self.params[0])
        op2 = self.computer.get(self.params[1])

        res = self.func(op1, op2)

        self.computer.put(self.params[2], res)

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
        self.computer.put(self.params[0], input_value)

    @classmethod
    def num_args(cls):
        return 1


class OutputInstruction(Instruction):

    def execute(self):
        val = self.computer[self.params[0]]
        self.computer.output(val)

    @classmethod
    def num_args(cls):
        return 1
