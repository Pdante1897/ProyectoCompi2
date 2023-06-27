from ..Expresiones.Primitivos import Primitivos
from ..Expresiones.Identificadores import Identificador
from ..Instrucciones.Asignaciones import Asignacion_Variables
from ..Instrucciones.Declarar_variables import Declaracion_Variables4
from ..Instrucciones.arrays import Arrays
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos

class ForArray(Abstract):

    def __init__(self, id, arreglo, bloqueFor, fila, columna):
        self.id = id
        self.arreglo = arreglo

        self.bloqueFor = bloqueFor
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO
        
        variable = Declaracion_Variables4(self.id, self.fila, self.columna)
        variable = variable.interpretar(arbol, nuevaTabla)

        if type(self.arreglo) is str:
            arreglo = tabla.getTabla(self.arreglo)
            if arreglo is None: return Error("Semantico", "Variable Inexistente", self.fila, self.columna)
            arreglo= arreglo.valor.values
        
        elif isinstance(self.arreglo, Primitivos):
            if self.arreglo.tipo == "string": 
                arreglo = []
                for caracter in list(self.arreglo.interpretar(arbol, tabla)):
                    arreglo.append(Primitivos("string", caracter, self.fila, self.columna))
            else : return Error("Semantico", "Variable Inexistente", self.fila, self.columna)
        else:
            arreglo = self.arreglo

        if arreglo is None: return Error("Semantico", "No es un arreglo", self.fila, self.columna)
        
        if isinstance(variable, Error): return variable
        
        if isinstance(arreglo, Arrays): print("es array")
        print(arreglo)
        contador = 0
        arraylen = len(arreglo)
        print(self.arreglo)
        print(arreglo[0])
        
        while contador < arraylen - 1:
            print(contador)
            actualizar = Asignacion_Variables(self.id, arreglo[contador], self.fila, self.columna)
            print(actualizar.ide)
            actualizar = actualizar.interpretar(arbol, nuevaTabla)
            if isinstance(actualizar, Error): 
                print("error2")
                return actualizar
            for instruccion in self.bloqueFor:
                result = instruccion.interpretar(arbol, nuevaTabla)
                if isinstance(result, Return): return result
                if isinstance(result, Continue):  break
                if isinstance(result, Break): return None
                if isinstance(result, Error):
                    arbol.errores.append(result)
                    print("error1")
            print("--------------------------------------")
            print(nuevaTabla.getTabla(self.id).valor)
            print("--------------------------------------")
            contador = contador + 1
        return None
            


