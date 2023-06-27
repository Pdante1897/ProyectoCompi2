from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class For(Abstract):

    def __init__(self, inicio, condicion, aumento, bloqueFor, fila, columna):
        self.inicio = inicio
        self.condicion = condicion
        self.aumento = aumento
        self.bloqueFor = bloqueFor
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO

        inicio = self.inicio.interpretar(arbol, nuevaTabla)
        if isinstance(inicio, Error): return inicio

        condicion = self.condicion.interpretar(arbol, nuevaTabla)
        if isinstance(condicion, Error): return condicion
        # Validar que el tipo sea booleano
        if self.condicion.tipo != 'boolean':
            return Error("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
        # Recorriendo las instrucciones
        while condicion:
            for instruccion in self.bloqueFor:
                result = instruccion.interpretar(arbol, nuevaTabla)
                if isinstance(result, Return): return result
                if isinstance(result, Continue):  break
                if isinstance(result, Break): return None
                if isinstance(result, Error):
                    arbol.errores.append(result)
                    print("error1")
            nuevo_valor = self.aumento.interpretar(arbol, nuevaTabla)
            if isinstance(nuevo_valor, Error): 
                print("error2")
                return nuevo_valor
            
            
            print("--------------------------------------")
            print(nuevaTabla.getTabla(self.inicio.ide).ide)
            print("--------------------------------------")
            condicion = self.condicion.interpretar(arbol, nuevaTabla)
            if isinstance(condicion, Error): return condicion
            if self.condicion.tipo != 'boolean':
                return Error("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
        return None
            


