from ..Abstract.Abstracto import Abstract

class Continue(Abstract):

    def __init__(self, fila, columna):
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        return self