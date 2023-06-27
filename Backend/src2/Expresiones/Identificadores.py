from ..Abstract.retorno import Return
from ..Estructuras.generador import Generador
from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract

class Identificador(Abstract):
    def __init__(self, ide, fila, columna, tipo = None):
        self.ide = ide
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        super().__init__(fila, columna)

    def interpretar(self, arbol , tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Acceso")

        simbolo = tabla.getTabla(self.ide)
        if simbolo == None:
            generator.addComment("Fin de compilacion de Acceso por error")
            return Error("Semantico", "Variable no encontrada", self.fila, self.columna)
        # Temporal para guardar la variable
        temp = generator.addTemp()
        
        # Obtencion de posicion de la variable
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')
        generator.getStack(temp, tempPos)
            
        
        if simbolo.tipo != 'boolean':
            generator.addComment("Fin de compilacion de Acceso")
            generator.addSpace()
            return Return(temp, simbolo.tipo, True)
        
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()

        generator.addIf(temp,'1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)

        generator.addComment("Fin de compilacion de Acceso")
        generator.addSpace()

        ret = Return(None, 'boolean', True)
        ret.setTrueLbl(self.trueLbl)
        ret.setFalseLbl(self.falseLbl)
        return ret



    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide