from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.arbol import Arbol
from ..Estructuras.tablasimbolos import TablaSimbolos


class Arrays(Abstract):

    def __init__(self,id, expresion, fila, columna):
        self.id = id
        self.expresion = expresion
        super().__init__(fila, columna)
        
    def interpretar(self, arbol, tabla):
        if tabla.getTabla(self.expresion) != None:
            resultado = Error("Semantico", "Variable o funcion ya existente.", self.fila, self.columna)
            return resultado
        simbolo = Simbolo(self.id, "array", self.expresion, self.fila, self.columna)
        resultado = tabla.setTabla(simbolo)
        if isinstance(resultado, Error): return resultado
        return None
    

class Array(Abstract):

    def __init__(self, value, type):
        self.type = type
        self.value = value

    def toString(self):
        return str(self.value)

    def getValue(self):
        return self.value

    def getType(self):
        return self.type    

class DeclareArray(Abstract):

    def __init__(self, values, row, column):
        self.values = values
        self.row = row
        self.column = column

    def interpretar(self, tree, table):
        values = []
        for i in range(len(self.values)):
            value = self.values[i].interpretar(tree, table)
            values.append(value)
        return Array(values, "array")

    

class AssignArray(Abstract):

    def __init__(self, left, expr, type, auxType, row, column):
        self.left = left
        self.expr = expr
        self.type = type
        self.auxType = auxType
        self.row = row
        self.column = column

    def interpretar(self, tree, table):
        value = self.expr.interpretar(tree, table)
        assign = self.left.interpretar(tree, table)

        if assign is not None:
            if self.type != None:
                if self.type.type is not value.type:
                    Error("Semantico", "Los tipos de datos no coinciden en la asignacion", self.row, self.column)
                    return
                else:
                    if self.type == "struct":
                        if self.auxType != value.auxType:
                            Error("Semantico", "Los tipos de datos no coinciden en la asignación", self.row, self.column)
                        return

            assign.value = value.value
            assign.type = value.type
        else:
            Error("Semantico", "No es posible acceder al arreglo", self.row, self.column)


class AccessArray(Abstract):

    def __init__(self, id, indexB, indexE, row, column):
        self.id = id
        self.indexB = indexB
        self.indexE = indexE
        self.row = row
        self.column = column

    def interpretar(self, tree, table):
        var = None
        result = None
        indexB = self.indexB.interpretar(tree, table)
        indexE = None

        if self.indexE is not None:
            indexE = self.indexE.interpretar(tree, table)

        if indexB.type == "number":
            if indexB.value > 0:
                if isinstance(self.id, AccessArray):
                    var = self.id.interpretar(tree, table)
                else:
                    var = table.getTable(self.id)
                if var is None:
                    Error("Semantico", "No existe la variable especificada", self.row, self.column)
                    return result
                try:
                    if var.value.getType() != "null":
                        if var.value.getType() == "array":
                            if indexE != None:
                                if indexE.type == "number":
                                    if indexB.value > 0:
                                        result.value = var.value.value[indexB.value - 1 : indexE.value - 1]
                                        result.type = "array"
                                        return result
                                    else:
                                        Error("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
                                        return result
                            else:
                                result =var.value.value[indexB.value-1]
                                return result
                        else:
                            Error("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Error("Semantico", "La variable es de tipo NOTHING", self.row, self.column)
                except:
                    if var.getType() != "null":
                        if var.getType() is "array":
                            if indexE != None:
                                if indexE.type == "number":
                                    if indexB.value > 0:
                                        result.value = var.value[indexB.value - 1 : indexE.value - 1]
                                        result.type = "array"
                                        return result
                                    else:
                                        Error("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
                                        return result
                            else:
                                result =var.value[indexB.value-1]
                                return result
                        else:
                            Error("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Error("Semantico", "La variable es de tipo NOTHING", self.row, self.column)
            else:
                Error("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
        else:
            Error("Semantico", "Los indicies de los ARRAYS deben ser tipo INTEGER", self.row, self.column)
        return result