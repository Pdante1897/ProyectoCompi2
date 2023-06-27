from ..Expresiones.Primitivos import Primitivos
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract, ObjectType
from ..Estructuras.Error import Error

class CreaStruct(Abstract):
    def __init__(self,id,attr,fila,columna):
        self.id = id
        self.attr = attr
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, arbol, tabla):
        tabla.GuardaStruct(self.id, self.attr)



class DeclareStruct(Abstract):
    def __init__(self, id, tipo, row, column):
        self.id = id
        self.tipo = tipo
        self.row = row
        self.column = column

    def interpretar(self, arbol, tabla):
        struct = tabla.getStruct(self.tipo)
        if struct == None:
            print("no existe tipo")
            return
        attrs = []
        for param in struct:
            ats = {}
            ats.update({
                'tipo' : param.get('tipo'),
                'id' : param.get('id'),
                'valor': "null"
            })
            attrs.append(ats)
        symbol = Simbolo(self.id, ObjectType.STRUCT, attrs,self.row, self.column)
        tabla.updateTableStruct(symbol)


class DeclareStruct2(Abstract):
    def __init__(self, id, tipo, atributos, row, column):
        self.id = id
        self.tipo = tipo
        self.atributos = atributos
        self.row = row
        self.column = column

    def interpretar(self, arbol, tabla):
        struct = tabla.getStruct(self.tipo)
        if struct == None:
            print("no existe tipo")
            return
        if len(self.atributos) != len(struct):
            return Error("Semantico", "Atributos no coinciden.", self.row, self.column)
        var = []
        for atri in self.atributos:
            expresion = atri.get('expresion').interpretar(arbol, tabla)
            if isinstance(expresion, Primitivos):
                expresion = expresion.valor
            var.append(expresion)
        cont = 0
        
        attrs = []
        for param in struct:
            ats = {}
            ats.update({
                'tipo' : param.get('tipo'),
                'id' : param.get('id'),
                'valor': var[cont]
            })
            cont = cont + 1

            attrs.append(ats)
        
        symbol = Simbolo(self.id, ObjectType.STRUCT, attrs,self.row, self.column)
        tabla.updateTableStruct(symbol)