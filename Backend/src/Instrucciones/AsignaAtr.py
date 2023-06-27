from ..Abstract.Abstracto import Abstract
from .. Abstract.Abstracto import ObjectType
from ..Instrucciones.AccesoS import AccesoS
from ..Instrucciones.Struct import Struct


class AsignaAttr(Abstract):
    def __init__(self, id, expre, fila, columna):
        self.id = id
        self.expre = expre
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, arbol, tabla):
        
        if isinstance(self.id, AccesoS):
            var = self.id.interpretar(arbol, tabla)
        else:
            var = tabla.getTabla(self.id)
        value = self.expre.interpretar(arbol,tabla)
        if isinstance(value, Struct):
            print("Este es un struct")
            var.value = {}
            for name,val in value.value.items():
                var.value[name] = val.value
            var.type = ObjectType.STRUCT
        else:
            var.value = value.value
            var.type = value.type