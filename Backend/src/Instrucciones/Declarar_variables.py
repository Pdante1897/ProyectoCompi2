from ..Instrucciones.AccesoA import AccessArray
from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract
from ..Estructuras.simbolo import Simbolo

class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if tabla.getTabla(self.ide) != None:
            resultado = Error("Semantico", "Variable ya existente.", self.fila, self.columna)
            return resultado
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        if str(self.tipo) == str(self.valor.tipo):
            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
            resultado = tabla.setTabla(simbolo)
            if isinstance(resultado, Error): return resultado
            return None
        else:
            resultado = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return resultado

class Declaracion_Variables2(Abstract):

    def __init__(self, ide, tipo, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if tabla.getTabla(self.ide) != None:
            resultado = Error("Semantico", "Variable ya existente.", self.fila, self.columna)
            return resultado
        simbolo = Simbolo(str(self.ide), self.tipo, "null", self.fila, self.columna)
        resultado = tabla.setTabla(simbolo)
        if isinstance(resultado, Error): return resultado
        return None
        

class Declaracion_Variables3(Abstract):

    def __init__(self, ide, valor, fila, columna):
        self.ide = ide # a
        self.tipo = None # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if tabla.getTabla(self.ide) != None:
            resultado = Error("Semantico", "Variable ya existente.", self.fila, self.columna)
            return resultado
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        if isinstance(self.valor, AccessArray):
            if type(value) is int: tipo = "number"
            elif type(value) is float: tipo = "number"
            elif type(value) is str: tipo = "string"
            elif type(value) is bool: tipo = "boolean"
        else: tipo = self.valor.tipo

        simbolo = Simbolo(str(self.ide), tipo, value, self.fila, self.columna)
        resultado = tabla.setTabla(simbolo)
        if isinstance(resultado, Error): return resultado
        return None
        
class Declaracion_Variables4(Abstract):

    def __init__(self, ide, fila, columna):
        self.ide = ide # a
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if tabla.getTabla(self.ide) != None:
            resultado = Error("Semantico", "Variable ya existente.", self.fila, self.columna)
            return resultado
        simbolo = Simbolo(str(self.ide), "any", "null", self.fila, self.columna)
        resultado = tabla.setTabla(simbolo)
        if isinstance(resultado, Error): return resultado
        return None
    
