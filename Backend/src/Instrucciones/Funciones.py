from ..Instrucciones.Return import Return
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class Metodo(Abstract):

    def __init__(self, ide, parametros, instrucciones, fila, columna):
        self.ide = ide
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = 'void'
        super().__init__(fila, columna)
    

    def interpretar(self, arbol, tabla):
        entorno = TablaSimbolos(tabla)
        for instruccion in self.instrucciones:
            print(instruccion)
            value = instruccion.interpretar(arbol, entorno)
            if isinstance(value, Error): return value
            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.value
        return None

class Llamada(Abstract):

    def __init__(self, ide, parametros, fila, columna):
        self.ide = ide
        self.parametros = parametros
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        print("aqui")
        result = arbol.getFuncion(self.ide)
        if result == None:
            return Error("Semantico", "No se encontro la funcion: " + str(self.ide), str(self.fila), str(self.columna))
        entorno = TablaSimbolos(arbol.getTsglobal())
        print(result.parametros)
        print(self.parametros)

        if result.parametros == None: result.parametros = []
        if self.parametros == None: self.parametros = []

        if len(self.parametros) == len(result.parametros):
        
            contador = 0
            for expresion in self.parametros:
                resultE = expresion.interpretar(arbol, tabla)
                if isinstance(resultE, Error): return resultE
                if result.parametros[contador]['tipo'] == expresion.tipo or result.parametros[contador]['tipo'] == "any":
                    simbolo = Simbolo(str(result.parametros[contador]['id']), expresion.tipo, resultE, self.fila, self.columna)
                    resultT = entorno.setTablaFuncion(simbolo)
                    if isinstance(resultT, Error): return resultT
                else:
                    return Error("Semantico", "Tipo de dato diferente en Parametros", str(self.fila), str(self.columna))
                contador += 1

        value = result.interpretar(arbol, entorno) # me puede retornar un valor
        if isinstance(value, Error): return value
        self.tipo = result.tipo
        if value is None:
            return "null"
        return value