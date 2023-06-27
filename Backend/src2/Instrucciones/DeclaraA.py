from ..Abstract.Abstracto import Abstract
from ..Abstract.Abstracto import ObjectType
from ..Object.Array import Array

class DeclareArray(Abstract):

    def __init__(self, values, row, column):
        self.values = values
        self.row = row
        self.column = column

    def interpretate(self, tree, table):
        values = []
        for i in range(len(self.values)):
            value = self.values[i].interpretate(tree, table)
            values.append(value)
        return Array(values, ObjectType.ARRAY)