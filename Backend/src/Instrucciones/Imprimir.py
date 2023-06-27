from ..Instrucciones.DeclaraA import DeclareArray
from ..Instrucciones.AccesoS import AccesoS
from ..Expresiones.Identificadores import Identificador
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Expresiones.Primitivos import Primitivos
class Imprimir(Abstract):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion # <<Class.Primitivos>>
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        value = self.expresion.interpretar(arbol, tabla)
        if isinstance(value, Primitivos): 
                value = value.valor
        if isinstance(value, DeclareArray): 
                auxiliar = []
                for valores in value.values:
                     auxiliar.append(valores.interpretar(arbol, tabla))
                value = auxiliar    
        if isinstance(value, Error): 
            print("aquii")
            return value         
        #print(value)
        arbol.updateConsola(str(value))
        return value
    
class Imprimir2(Abstract):

    def __init__(self, listaexp, fila, columna):
        self.listaexp = listaexp 
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        valor = ""
        for expresiones in self.listaexp:
            value = expresiones.interpretar(arbol, tabla)
            if isinstance(value, Primitivos): 
                value = value.valor
            if isinstance(value, DeclareArray): 
                auxiliar = []
                for valores in value.values:
                     auxiliar.append(valores.interpretar(arbol, tabla))
                value = auxiliar   
            if isinstance(value, Error): 
                return value         
            #print(value)
            valor += str(value) + " "
        arbol.updateConsola(str(valor))
        return valor