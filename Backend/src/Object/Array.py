from ..Abstract.Abstracto import Abstract

class Array(Abstract):

    def __init__(self, value, type):
        self.type = type
        self.value = value

    def toString(self):
        return str(self.value)

    def getValue(self):
        return self.value

    def getType(self):
        return self.type
