from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract
from ..Estructuras.simbolo import Simbolo

class Asignacion_Variables(Abstract):

    def __init__(self, ide, valor, fila, columna):
        self.ide = ide # a
        self.tipo = None # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        valorAnt = tabla.getTabla(self.ide)
        if valorAnt == None: return Error("Semantico", "Variable no declarada.", self.fila, self.columna)
        if str(valorAnt.tipo) == str(self.valor.tipo):
            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
            resultado = tabla.updateTabla(simbolo)
            if isinstance(resultado, Error): return resultado
            return None
        elif str(valorAnt.tipo) == "any":
            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
            resultado = tabla.updateTabla(simbolo)
            if isinstance(resultado, Error): return resultado
            return None
        else:
            resultado = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return resultado
        
class Asignacion_incrementable(Abstract):

    def __init__(self, ide, aumento, fila, columna):
        self.ide = ide # a
        self.aumento = aumento
        super().__init__(fila, columna)


    def interpretar(self, arbol, tabla):
        valorAct = tabla.getTabla(self.ide)
        if valorAct == None :
            resultado = Error("Semantico", "Variable no declarada.", self.fila, self.columna)
            return resultado
        if valorAct.tipo != "number":
            print("aquiiii" + valorAct.tipo)
            resultado = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return resultado
        simbolo = Simbolo(self.ide, valorAct.tipo, valorAct.valor + self.aumento, self.fila, self.columna)
        resultado = tabla.updateTabla(simbolo)
        if isinstance(resultado, Error): return resultado
        return None