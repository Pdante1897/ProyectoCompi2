from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Expresiones.Primitivos import Primitivos
from ..Abstract.Abstracto import ObjectType
from ..Instrucciones.struct import Struct
from ..Instrucciones.Return import Return
from ..Estructuras.Error import Error

class AccesoS(Abstract):
    def __init__(self, id, atributo, fila, columna):
        self.id = id
        self.atributo = atributo
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, arbol, tabla):
        var = None
        result = "null"
        res = None
        if isinstance(self.id, AccesoS):
            var = self.id.interpretar(arbol, tabla)
        else:
            var = tabla.getTabla(self.id)
            print(var.valor)
        
        if var is not None or var is not Error:
            print("pausa1")
            print(var)
            print("acceso1")
        if isinstance(var, Simbolo):
            for parametros in var.valor:
                print("parametro---")
                print(parametros)
                if parametros.get('id') == self.atributo:
                    var = Primitivos(parametros.get('tipo'), parametros.get('valor'), self.fila, self.columna)
            if not isinstance(var.valor, dict):
                result = var
                res = var.valor


            else:
                Error("Semantico", "La propiedad que se intenta acceder no es de un tipo válida", self.fila, self.columna)
        print("acceso")
        print("res")
        print(res)
        return var
