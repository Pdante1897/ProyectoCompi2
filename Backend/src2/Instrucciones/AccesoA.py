from ..Abstract.Abstracto import Abstract
from ..Object.Primitive import Primitive
from ..Abstract.Abstracto import ObjectType

class AccessArray(Abstract):

    def __init__(self, id, indexB, indexE, row, column):
        self.id = id
        self.indexB = indexB
        self.indexE = indexE
        self.row = row
        self.column = column

    def interpretate(self, arbol, tabla):
        var = None
        result = Primitive(ObjectType.NULL, None)
        indexB = self.indexB.interpretate(arbol, tabla)
        indexE = None

        if self.indexE is not None:
            indexE = self.indexE.interpretate(arbol, tabla)

        if indexB.type is ObjectType.INTEGER:
            if indexB.value > 0:
                if isinstance(self.id, AccessArray):
                    var = self.id.interpretate(arbol, tabla)
                else:
                    var = tabla.getTabla(self.id)
                if var is None:
                    Exception("Semantico", "No existe la variable especificada", self.row, self.column)
                    return result
                try:
                    if var.value.getType() != ObjectType.NULL:
                        if var.value.getType() is ObjectType.ARRAY:
                            if indexE != None:
                                if indexE.type == ObjectType.INTEGER:
                                    if indexB.value > 0:
                                        result.value = var.value.value[indexB.value - 1 : indexE.value - 1]
                                        result.type = ObjectType.ARRAY
                                        return result
                                    else:
                                        Exception("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
                                        return result
                            else:
                                result =var.value.value[indexB.value-1]
                                return result
                        else:
                            Exception("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Exception("Semantico", "La variable es de tipo NOTHING", self.row, self.column)
                except:
                    if var.getType() != ObjectType.NULL:
                        if var.getType() is ObjectType.ARRAY:
                            if indexE != None:
                                if indexE.type == ObjectType.INTEGER:
                                    if indexB.value > 0:
                                        result.value = var.value[indexB.value - 1 : indexE.value - 1]
                                        result.type = ObjectType.ARRAY
                                        return result
                                    else:
                                        Exception("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
                                        return result
                            else:
                                result =var.value[indexB.value-1]
                                return result
                        else:
                            Exception("Semantico", "La variable no es un ARRAY", self.row, self.column)
                    else:
                        Exception("Semantico", "La variable es de tipo NOTHING", self.row, self.column)
            else:
                Exception("Semantico", "Indice de ARRAY debe ser mayor a 0", self.row, self.column)
        else:
            Exception("Semantico", "Los indicies de los ARRAYS deben ser tipo INTEGER", self.row, self.column)
        return result