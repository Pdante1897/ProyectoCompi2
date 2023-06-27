from ..Abstract.Abstracto import Abstract
from ..Abstract.Abstracto import ObjectType
from ..Instrucciones.arrays import Arrays

class DeclareArray(Abstract):

    def __init__(self, values, fila, columna):
        self.values = values
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, tabla):
        values = []
        for i in range(len(self.values)):
            value = self.values[i].interpretar(arbol, tabla)
            values.append(value)
        return Arrays(None, values,self.fila,self.columna)