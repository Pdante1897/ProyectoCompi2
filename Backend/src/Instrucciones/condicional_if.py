
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class If(Abstract):

    def __init__(self, condicion, bloqueIf, bloqueElse, bloqueElseif, fila, columna):
        self.condicion = condicion
        self.bloqueIf = bloqueIf
        self.bloqueElse = bloqueElse
        self.bloqueElseif = bloqueElseif
        super().__init__(fila, columna)
    

    def interpretar(self, arbol, tabla):
        condicion = self.condicion.interpretar(arbol, tabla)
        if isinstance(condicion, Error): return condicion
        # Validar que el tipo sea booleano
        if bool(condicion) == True:
            entorno = TablaSimbolos(tabla)  #NUEVO ENTORNO - HIJO - Vacio
            for instruccion in self.bloqueIf:
                result = instruccion.interpretar(arbol, entorno) 
                if isinstance(result, Error) :
                    arbol.setErrores(result)
                if isinstance(result, Return): return result
                if isinstance(result, Break): return result
                if isinstance(result, Continue):return result
        elif self.bloqueElse != None:
            entorno = TablaSimbolos(tabla)
            for instruccion in self.bloqueElse:
                result = instruccion.interpretar(arbol, entorno) 
                if isinstance(result, Error) :
                    arbol.setErrores(result)
                if isinstance(result, Return): return result
                if isinstance(result, Break): return result
                if isinstance(result, Continue):return result
        elif self.bloqueElseif != None:
            result = self.bloqueElseif.interpretar(arbol, tabla)
            if isinstance(result, Error) : return result
            if isinstance(result, Return): return result
            if isinstance(result, Break): return result
            if isinstance(result, Continue):return result