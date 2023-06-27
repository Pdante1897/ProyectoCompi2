from ..Estructuras.generador import Generador
from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract
from ..Estructuras.simbolo import Simbolo

class Asignacion_Variables(Abstract):

    def __init__(self, ide, valor, fila, columna):
        self.ide = ide # a
        self.valor = valor # 4, 'hola', true
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de asignacion de valor de variable')
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        simbolo = tabla.getTabla(self.ide)

        if str(simbolo.tipo) != str(self.valor.tipo):
            generator.addComment('Error, tipo de dato diferente declarado.')
            result = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return result
        
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')
        
        if value.getTipo() == 'boolean':
            tempLbl = generator.newLabel()
            
            generator.putLabel(value.trueLbl)
            generator.setStack(tempPos, "1")
            
            generator.addGoto(tempLbl)

            generator.putLabel(value.falseLbl)
            generator.setStack(tempPos, "0")

            generator.putLabel(tempLbl)
        else:
            generator.setStack(tempPos, value.value)
            print(value.value)
        generator.addComment('Fin de compilacion de asignacion de valor de variable')
        
class Asignacion_incrementable(Abstract):

    def __init__(self, ide, aumento, fila, columna):
        self.ide = ide # a
        self.aumento = aumento
        super().__init__(fila, columna)


    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment('Compilacion de asignacion de aumento de variable')
        resultado = None
        valorAct = tabla.getTabla(self.ide)
        if valorAct == None :
            resultado = Error("Semantico", "Variable no declarada.", self.fila, self.columna)
            return resultado
        if valorAct.tipo != "number":
            print("aquiiii" + valorAct.tipo)
            resultado = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return resultado
        tempPos = valorAct.pos
        if not valorAct.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', valorAct.pos, '+')
        generator.setStackAu(tempPos, self.aumento)
        generator.addComment('Fin de compilacion de asignacion de aumento de variable')
        
        if isinstance(resultado, Error): return resultado
        return None
    
        

        
        simbolo = tabla.getTabla(self.ide)

        if str(simbolo.tipo) != str(self.valor.tipo):
            generator.addComment('Error, tipo de dato diferente declarado.')
            result = Error("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return result
        
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')
        
        if value.getTipo() == 'boolean':
            tempLbl = generator.newLabel()
            
            generator.putLabel(value.trueLbl)
            generator.setStack(tempPos, "1")
            
            generator.addGoto(tempLbl)

            generator.putLabel(value.falseLbl)
            generator.setStack(tempPos, "0")

            generator.putLabel(tempLbl)
        else:
            generator.setStack(tempPos, value.value)
            print(value.value)
        generator.addComment('Fin de compilacion de asignacion de valor de variable')