from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class Return(Abstract):

    def __init__(self,expresion, fila, columna):
        self.expresion = expresion
        self.value = None
        self.tipo = None
        self.trueLbl = ''
        self.falseLbl = ''
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        result = self.expresion.interpretar(arbol, tabla)
        if isinstance(result, Error): return result
        self.tipo = result.getTipo()
        self.value = result.getValue()
        if self.tipo == 'boolean':
            self.trueLbl = result.getTrueLbl()
            self.falseLbl = result.getFalseLbl()
            
        return self

    def getValor(self):
        return self.value
    def getTipo(self):
        return self.tipo
    def getTrueLbl(self):
        return self.trueLbl
    
    def getFalseLbl(self):
        return self.falseLbl
    
    def setValor(self, valor):
        self.valor = valor
    
    def setTipo(self, tipo):
        self.tipo  = tipo
    
    def setTrueLbl(self, lbl):
        self.trueLbl = lbl
    def setFalseLbl(self, lbl):
        self.falseLbl = lbl