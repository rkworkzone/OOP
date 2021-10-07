from abc import ABCMeta, abstractmethod


class AbstractOperation(object):
    __metaclass__ = ABCMeta

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()

    @abstractmethod
    def execute(self):
        pass


a = AbstractOperation(1,2)

class ConcreteOperation(AbstractOperation):
    pass

#c = ConcreteOperation(1,2)


class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b


class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b


class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operand_a * self.operand_b


class DivideOperation(AbstractOperation):
    def execute(self):
        return self.operand_a / self.operand_b


operation = AddOperation(1, 2)
print  operation.execute()