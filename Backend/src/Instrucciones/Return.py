from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class Return(Abstract):

    def __init__(self,expresion, fila, columna):
        self.expresion = expresion
        self.value = None
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if self.expresion == None: return None
        result = self.expresion.interpretar(arbol, tabla)
        if isinstance(result, Error): return result
        self.tipo = self.expresion.tipo
        self.value = result
        return self