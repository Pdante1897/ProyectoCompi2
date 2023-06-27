from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class CreaStruct(Abstract):
    def __init__(self, id, atributo, fila, columna):
        self.id = id
        self.atributo = atributo
        self.valor = [] 

        super().__init__(fila, columna)
        
        
    def interpretar(self, arbol, tabla):
        tabla.GuardaStruct(self.id, self.atributo)

    

        