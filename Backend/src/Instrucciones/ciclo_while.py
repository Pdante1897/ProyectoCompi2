
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.arbol import Arbol
from ..Estructuras.tablasimbolos import TablaSimbolos


class While(Abstract):

    def __init__(self, condicion, bloqueWhile, fila, columna):
        self.condicion = condicion
        self.bloqueWhile = bloqueWhile
        super().__init__(fila, columna)
    
    
    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO

        #inicio = self.inicio.interpretar(arbol, nuevaTabla)
        #if isinstance(inicio, Error): return inicio

        condicion = self.condicion.interpretar(arbol, tabla)
        if isinstance(condicion, Error): return condicion
        
        if self.condicion.tipo != 'boolean':
            return Error("Semantico", "Tipo de dato no booleano en while.", self.fila, self.columna)
        # Recorriendo las instrucciones
        while bool(condicion)==True:
            for instruccion in self.bloqueWhile:
                result = instruccion.interpretar(arbol, nuevaTabla)
                if isinstance(result, Error):
                    arbol.Errores.append(result)
                if isinstance(result, Return): return result
                if isinstance(result, Continue):  break
                if isinstance(result, Break): return None

            #nuevo_valor = self.aumento.interpretar(arbol, nuevaTabla)
            #if isinstance(nuevo_valor, Error): return nuevo_valor    
            condicion = self.condicion.interpretar(arbol, nuevaTabla)
            if isinstance(condicion, Error): return condicion
            if self.condicion.tipo != 'boolean':
                return Error("Semantico", "Tipo de dato no booleano en WHILE.", self.fila, self.columna)
        return None