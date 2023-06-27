from ..Expresiones.Primitivos import Primitivos
from ..Instrucciones.struct import Struct
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract, ObjectType
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos
from ..Instrucciones.AccesoS import AccesoS



class AsignaStruct(Abstract):
    def __init__(self, id, parametro, expresion, fila, columna):
        self.id = id
        self.parametro = parametro
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
    def interpretar(self, arbol, tabla):
        struct = tabla.getTabla(self.id)
        if struct.getTipo() != ObjectType.STRUCT:
            print("No es Struct")
            return        
        expresion = self.expresion.interpretar(arbol, tabla)
        if struct == None:
            print("no existe el struct")
            return
        
        expresion = self.expresion.interpretar(arbol, tabla)
        if isinstance(expresion, Primitivos):
                expresion = expresion.valor
        cont = 0
        attrs = []
        for param in struct.valor:
            ats = {}
            if param.get('id') == self.parametro:
                ats.update({
                    'tipo' : param.get('tipo'),
                    'id' : param.get('id'),
                    'valor': expresion
                })
                attrs.append(ats)
                continue
            attrs.append(param)
        
        symbol = Simbolo(self.id, ObjectType.STRUCT, attrs,self.fila, self.columna)
        tabla.updateTableStruct(symbol)