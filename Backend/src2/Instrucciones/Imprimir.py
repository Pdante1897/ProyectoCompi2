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
        gen = genAux.getInstance()
        value = self.expresion.interpretar(arbol, tabla)
        print("valor imp ", value.value)
        print("valor tipo aux ", value.getTipoAux())

        if isinstance(value, Error): return value

        if value.getTipo() == 'number':
            gen.addPrint('f', value.getValue())
        elif value.getTipo() == 'string' or value.getTipo() == 'any':
            gen.fPrintString()

            paramTemp = gen.addTemp()
            
            gen.addExp(paramTemp, 'P', tabla.size, '+')
            gen.addExp(paramTemp, paramTemp, '1', '+')
            gen.setStack(paramTemp, value.value)
            
            gen.newEnv(tabla.size)
            gen.callFun('printString')

            temp = gen.addTemp()
            gen.getStack(temp, 'P')
            gen.retEnv(tabla.size)
        elif value.getTipo() == 'array':
            if value.getTipoAux() == 'acceso':
                gen.addPrint('f', value.getValue())
            else :
                gen.fPrintArray()
                paramTemp = gen.addTemp()
                gen.addExp(paramTemp, 'P', tabla.size, '+')
                gen.addExp(paramTemp, paramTemp, '1', '+')
                gen.setStack(paramTemp, value.value)
            
                gen.newEnv(tabla.size)
                gen.addPrint('c' ,91)
                gen.callFun('printArray')
                gen.addPrint('c' , 93)

                temp = gen.addTemp()
                gen.getStack(temp, 'P')
                gen.retEnv(tabla.size)
        elif value.getTipo() == 'boolean':
            tempLbl = gen.newLabel()

            gen.putLabel(value.getTrueLbl())
            gen.printTrue()

            gen.addGoto(tempLbl)

            gen.putLabel(value.getFalseLbl())
            gen.printFalse()

            gen.putLabel(tempLbl)

        gen.addPrint('c', 10)
    
class Imprimir2(Abstract):

    def __init__(self, listaexp, fila, columna):
        self.listaexp = listaexp 
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        valor = ""
        genAux = Generador()
        gen = genAux.getInstance()
        for expresiones in self.listaexp:
       
            value = expresiones.interpretar(arbol, tabla)

            if isinstance(value, Error): return value

            if value.getTipo() == 'number':
                gen.addPrint('f', value.getValue())
            elif value.getTipo() == 'string' or value.getTipo() == 'any':
                gen.fPrintString()

                paramTemp = gen.addTemp()
            
                gen.addExp(paramTemp, 'P', tabla.size, '+')
                gen.addExp(paramTemp, paramTemp, '1', '+')
                gen.setStack(paramTemp, value.value)
            
                gen.newEnv(tabla.size)
                gen.callFun('printString')

                temp = gen.addTemp()
                gen.getStack(temp, 'P')
                gen.retEnv(tabla.size)
            elif value.getTipo() == 'array':
                if value.getTipoAux() == 'acceso':
                    gen.addPrint('f', value.getValue())
                else :
                    gen.fPrintArray()
                    paramTemp = gen.addTemp()
                    gen.addExp(paramTemp, 'P', tabla.size, '+')
                    gen.addExp(paramTemp, paramTemp, '1', '+')
                    gen.setStack(paramTemp, value.value)
            
                    gen.newEnv(tabla.size)
                    gen.addPrint('c' ,91)
                    gen.callFun('printArray')
                    gen.addPrint('c' , 93)

                    temp = gen.addTemp()
                    gen.getStack(temp, 'P')
                    gen.retEnv(tabla.size)
            elif value.getTipo() == 'boolean':
                tempLbl = gen.newLabel()

                gen.putLabel(value.getTrueLbl())
                gen.printTrue()

                gen.addGoto(tempLbl)

                gen.putLabel(value.getFalseLbl())
                gen.printFalse()

                gen.putLabel(tempLbl)

            gen.addPrint('c', 32)
            
                   
        gen.addPrint('c', 10)
