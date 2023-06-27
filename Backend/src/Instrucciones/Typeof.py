from ..Expresiones.Primitivos import Primitivos
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error

class TypeOf(Abstract):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.tipo = "string"
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, tabla):
        auxiliar = None
        for valor in self.expresion:
            auxiliar = valor
            break
        value = auxiliar.interpretar(arbol, tabla)
        print(auxiliar.tipo)
        if isinstance(auxiliar, Error):
            return auxiliar
        
        return auxiliar.tipo