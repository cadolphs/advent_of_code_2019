from abc import ABCMeta, abstractmethod


class Instruction(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def num_args(cls):
        pass

    @abstractmethod
    def execute(self):
        pass


class HaltInstruction(Instruction):
    def __init__(self, computer):
        self.computer = computer

    def execute(self):
        self.computer.halt()

    @classmethod
    def num_args(cls):
        return 0


class DyadicOperation(Instruction):
    def __init__(self, computer, addr_src_1, addr_src_2, addr_tgt):
        self.computer = computer
        self.addr_src_1 = addr_src_1
        self.addr_src_2 = addr_src_2
        self.addr_tgt = addr_tgt

    def execute(self):
        op1 = self.computer.get(self.addr_src_1)
        op2 = self.computer.get(self.addr_src_2)

        res = self.func(op1, op2)

        self.computer.put(self.addr_tgt, res)

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
    def __init__(self, computer, addr_tgt):
        self.computer = computer
        self.addr_tgt = addr_tgt

    def execute(self):
        input_value = self.computer.read_input()
        self.computer.put(self.addr_tgt, input_value)

    @classmethod
    def num_args(cls):
        return 1


class OutputInstruction(Instruction):

    def __init__(self, computer, addr_src):
        self.computer = computer
        self.addr_src = addr_src

    def execute(self):
        val = self.computer[self.addr_src]
        self.computer.output(val)

    @classmethod
    def num_args(cls):
        return 1
