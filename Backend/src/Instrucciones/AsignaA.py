from ..Abstract.Abstracto import Abstract
from ..Abstract.Abstracto import ObjectType


class AssignArray(Abstract):

    def __init__(self, left, expr, type, auxType, row, column):
        self.left = left
        self.expr = expr
        self.type = type
        self.auxType = auxType
        self.row = row
        self.column = column

    def interpretate(self, tree, table):
        value = self.expr.interpretate(tree, table)
        assign = self.left.interpretate(tree, table)

        if assign is not None:
            if self.type != None:
                if self.type.type is not value.type:
                    Exception("Semantico", "Los tipos de datos no coinciden en la asignacion", self.row, self.column)
                    return
                else:
                    if self.type is ObjectType.STRUCT:
                        if self.auxType != value.auxType:
                            Exception("Semantico", "Los tipos de datos no coinciden en la asignación", self.row, self.column)
                        return

            assign.value = value.value
            assign.type = value.type
        else:
            Exception("Semantico", "No es posible acceder al arreglo", self.row, self.column)
