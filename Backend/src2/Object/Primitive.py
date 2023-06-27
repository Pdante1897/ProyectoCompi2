from ..Abstract.Abstracto import Abstract


class Primitive(Abstract):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def toString(self):
        return str(self.value)

    def getValue(self):
        return self.value

    def getType(self):
        return self.type