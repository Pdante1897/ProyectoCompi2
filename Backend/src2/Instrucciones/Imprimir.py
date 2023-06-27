from ..Instrucciones.AccesoS import AccesoS
from ..Expresiones.Identificadores import Identificador
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Estructuras.generador import Generador
from ..Expresiones.Primitivos import Primitivos
class Imprimir(Abstract):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion # <<Class.Primitivos>>
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        value = self.expresion.interpretar(arbol, tabla)

        if isinstance(value, Error): return value

        if value.getTipo() == 'number':
            generator.addPrint('f', value.getValue())
        elif value.getTipo() == 'string' or value.getTipo() == 'any':
            generator.fPrintString()

            paramTemp = generator.addTemp()
            
            generator.addExp(paramTemp, 'P', tabla.size, '+')
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, value.value)
            
            generator.newEnv(tabla.size)
            generator.callFun('printString')

            temp = generator.addTemp()
            generator.getStack(temp, 'P')
            generator.retEnv(tabla.size)
        elif value.getTipo() == 'boolean':
            tempLbl = generator.newLabel()

            generator.putLabel(value.getTrueLbl())
            generator.printTrue()

            generator.addGoto(tempLbl)

            generator.putLabel(value.getFalseLbl())
            generator.printFalse()

            generator.putLabel(tempLbl)

        generator.addPrint('c', 10)
    
class Imprimir2(Abstract):

    def __init__(self, listaexp, fila, columna):
        self.listaexp = listaexp 
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        valor = ""
        genAux = Generador()
        generator = genAux.getInstance()
        for expresiones in self.listaexp:
       
            value = expresiones.interpretar(arbol, tabla)

            if isinstance(value, Error): return value

            if value.getTipo() == 'number':
                generator.addPrint('f', value.getValue())
            elif value.getTipo() == 'string' or value.getTipo() == 'any':
                generator.fPrintString()

                paramTemp = generator.addTemp()
            
                generator.addExp(paramTemp, 'P', tabla.size, '+')
                generator.addExp(paramTemp, paramTemp, '1', '+')
                generator.setStack(paramTemp, value.value)
            
                generator.newEnv(tabla.size)
                generator.callFun('printString')

                temp = generator.addTemp()
                generator.getStack(temp, 'P')
                generator.retEnv(tabla.size)
            elif value.getTipo() == 'boolean':
                tempLbl = generator.newLabel()

                generator.putLabel(value.getTrueLbl())
                generator.printTrue()

                generator.addGoto(tempLbl)

                generator.putLabel(value.getFalseLbl())
                generator.printFalse()

                generator.putLabel(tempLbl)

            generator.addPrint('c', 32)
            
                   
        generator.addPrint('c', 10)
