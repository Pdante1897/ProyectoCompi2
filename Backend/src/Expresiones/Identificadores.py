from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract

class Identificador(Abstract):
    def __init__(self, identificador, fila, columna, tipo = None):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def interpretar(self, arbol , tabla):
        simbolo = tabla.getTabla(self.identificador)
        if simbolo == None:
            return Error("Semantico", "Variable no encontrada", self.fila, self.columna)
        self.tipo = simbolo.getTipo()
        return simbolo.getValor()

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.identificador