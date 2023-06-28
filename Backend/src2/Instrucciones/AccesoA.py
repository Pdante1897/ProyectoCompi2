from ..Expresiones.Primitivos import Primitivos
from ..Expresiones.Identificadores import Identificador
from ..Abstract.retorno import Return
from ..Estructuras.Error import Error
from ..Estructuras.generador import Generador
from ..Abstract.Abstracto import Abstract
from ..Object.Primitive import Primitive
from ..Abstract.Abstracto import ObjectType

class AccessArray(Abstract):

    def __init__(self, ide, indexB, indexE, fila, columna):
        self.ide = ide
        self.indexB = indexB
        self.indexE = indexE
        self.fila = fila
        self.columna = columna

    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        indice = 0
        if isinstance(self.indexB, int) or  isinstance(self.indexB, float): indice = self.indexB
        if isinstance(self.indexB, Return): indice = self.indexB.value
        if isinstance(self.indexB, Primitivos): indice = self.indexB.interpretar(arbol, tabla).value
        if isinstance(self.indexB, Identificador):  
            indice = self.indexB.interpretar(arbol, tabla).value
        generator.addComment("Compilacion de Acceso Array")
        print("valor index: ", self.indexB)
        print("valor indice: ", indice)
        returnLbl = generator.newLabel()

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
            generator.addExp(tempPos, 'P', simbolo.pos , '+')
        tempA = generator.addTemp()
        generator.getStack(temp, tempPos)
        generator.addIdent()
        generator.addExp(tempA, temp, indice , '+')
        generator.addExp(tempA, tempA, '1' , '+')
        tempB = generator.addTemp()
        generator.getHeap(tempB, tempA)
        generator.addIdent()


        if simbolo.tipo != 'boolean':

            generator.addComment("Fin de compilacion de Acceso Array")
            generator.addSpace()
            
            print("llega al return")
            return Return(tempB, simbolo.tipo, True, 'acceso')
        
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()

        generator.addIf(temp,'1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)

        generator.addComment("Fin de compilacion de Acceso Array")
        generator.addSpace()

        ret = Return(None, 'boolean', True, 'acceso')
        ret.setTrueLbl(self.trueLbl)
        ret.setFalseLbl(self.falseLbl)
        return ret



    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide