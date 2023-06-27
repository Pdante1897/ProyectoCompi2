from ..Expresiones.Primitivos import Primitivos
from ..Estructuras.Error import Error
from ..Abstract.Abstracto import Abstract
from ..Estructuras.simbolo import Simbolo
from ..Estructuras.generador import Generador

class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        if str(self.tipo) == str(self.valor.tipo):
            inHeap = value.getTipo() == 'string' or value.getTipo() == 'interface'
            simbolo = tabla.setTabla(self.ide, value.getTipo(), inHeap , self.find)

        else:
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
        generator.addComment('Fin de compilacion de valor de variable')

class Declaracion_Variables2(Abstract):

    def __init__(self, ide, tipo, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = None # 4, 'hola', true
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        print("Aqui estoy")
        
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')
        val = None
        if self.tipo == "boolean": val = False        
        if self.tipo == "string": val = ""
        if self.tipo == "number": val = 0

        value = Primitivos(self.tipo, val, self.fila, self.columna).interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        inHeap = self.tipo == 'string' or self.tipo == 'interface'
        simbolo = tabla.setTabla(self.ide, self.tipo, inHeap , self.find)

        
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')
        
        if value.getTipo() == "boolean":
            tempLbl = generator.newLabel()
            
            generator.putLabel(value.trueLbl)
            generator.setStack(tempPos, "1")
            
            generator.addGoto(tempLbl)

            generator.putLabel(value.falseLbl)
            generator.setStack(tempPos, "0")

            generator.putLabel(tempLbl)
        else:
            generator.setStack(tempPos, value.value)
        generator.addComment('Fin de compilacion de valor de variable')
        

class Declaracion_Variables3(Abstract):

    def __init__(self, ide, valor, fila, columna):
        self.ide = ide # a
        self.tipo = None # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        inHeap = value.getTipo() == 'string' or value.getTipo() == 'interface'
        simbolo = tabla.setTabla(self.ide, value.getTipo(), inHeap , self.find)

        
        
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
        generator.addComment('Fin de compilacion de valor de variable')
        
class Declaracion_Variables4(Abstract):

    def __init__(self, ide, fila, columna):
        self.ide = ide # a
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        print("Aqui estoy")
        
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')

        value = Primitivos("any", "null", self.fila, self.columna).interpretar(arbol, tabla)
        if isinstance(value, Error): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        simbolo = tabla.setTabla(self.ide, "any", True , self.find)

        
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')
        
        generator.setStack(tempPos, value.value)
        generator.addComment('Fin de compilacion de valor de variable')
    
