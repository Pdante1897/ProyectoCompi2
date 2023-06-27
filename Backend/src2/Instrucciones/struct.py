from ..Abstract.Abstracto import Abstract


class Struct(Abstract):
    def __init__(self, tipo, auxTipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.auxTipo = auxTipo
        self.attributes = {}

    def toString(self):
        return str(self.valor)

    def getValor(self):
        return self.valor

    def getTipo(self):
        return self.tipo

    def getauxTipo(self):
        return self.auxTipo