from ..Expresiones.Identificadores import Identificador
from ..Abstract.Abstracto import Abstract
from ..Expresiones.Primitivos import Primitivos
from ..Estructuras.tablasimbolos import Error

class AccessArray(Abstract):

    def __init__(self, id, indexB, indexE, row, column):
        self.id = id
        self.indexB = indexB
        self.indexE = indexE
        self.row = row
        self.column = column

    def interpretar(self, arbol, tabla):
        var = None
        result = Primitivos("null", None , self.row, self.column)
        if not isinstance(self.indexB, Primitivos):
            indexB = self.indexB.interpretar(arbol, tabla)
            if type(indexB) is int or type(indexB) is float or type(indexB) is str or type(indexB) is bool:
                indexB= self.indexB
                indexB.valor = self.indexB.interpretar(arbol, tabla)
            if isinstance(self.indexB, Identificador):
                indexB = tabla.getTabla(self.indexB.identificador)
        else:
            indexB = self.indexB
        indexE = None
        if indexB is None:
            return Error("Semantico", "No existe la variable especificada", self.row, self.column)
        if self.indexE is not None:
            indexE = self.indexE.interpretar(arbol, tabla)
        print(self.indexB)
        print("index B :", indexB)
        if indexB.tipo == "number":
            print("primer if")
            if indexB.valor >= 0:
                print("segundo if")

                if isinstance(self.id, AccessArray):

                    var = self.id.interpretar(arbol, tabla)
                else:
                    var = tabla.getTabla(self.id)
                    print(var)
                if var is None:
                    Error("Semantico", "No existe la variable especificada", self.row, self.column)
                    return result
                try:
                    if var.valor.getTipo() != "null":
                        if var.valor.getTipo() == "array":
                            if indexE != None:
                                if indexE.tipo == "number":
                                    if indexB.valor >= 0:
                                        result.valor = var.valor.valor[indexB.valor - 1 : indexE.valor - 1]
                                        result.tipo = "array"
                                        return result
                                    else:
                                        Error("Semantico", "Indice de ARRAY debe ser mayor o igual a 0", self.row, self.column)
                                        return result
                            else:
                                result =var.valor.valor[indexB.valor-1]
                                return result
                        else:
                            Error("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Error("Semantico", "La variable es de tipo NOTHING", self.row, self.column)
                except:
                    if var.getTipo() != "null":
                        if var.getTipo() == "array":
                            if indexE != None:
                                if indexE.tipo == "number":
                                    if indexB.valor >= 0:
                                        result.valor = var.valor[indexB.valor - 1 : indexE.valor - 1]
                                        result.tipo = "array"
                                        return result
                                    else:
                                        Error("Semantico", "Indice de ARRAY debe ser mayor o igual a 0", self.row, self.column)
                                        return result
                            else:
                                #var = var.valor.interpretar(arbol, tabla)
                                #print(var)
                                var2 = var.valor.interpretar(arbol, tabla)
                                #print(var2)
                                #print(indexB.valor)
                                result =var2.expresion[int(indexB.valor)]
                                return result
                        else:
                            Error("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Error("Semantico", "La variable es de tipo NULL", self.row, self.column)
            else:
                Error("Semantico", "Indice de ARRAY debe ser mayor o igual a 0", self.row, self.column)
        else:
            Error("Semantico", "Los indicies de los ARRAYS deben ser tipo INTEGER", self.row, self.column)
        return result