from ..Instrucciones.Return import Return
from ..Abstract.retorno import Return as Return2

from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.tablasimbolos import TablaSimbolos
from ..Estructuras.generador import Generador
from typing import List

class Metodo(Abstract):

    def __init__(self, ide, parametros, instrucciones, tipo, fila, columna):
        self.ide = ide
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.recTemp = True
        super().__init__(fila, columna)
    

    def interpretar(self, arbol, tabla):
        funcion = arbol.setFunciones(self.ide, self)
        if funcion == 'error':
            error = Error("Semantico", f"Ya existe la funcion {self.ide}", self.fila, self.columna)
            return error
        
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment(f'Compilacion de la funcion {self.ide}')

        entorno = TablaSimbolos(tabla)

        Lblreturn = generador.newLabel()
        entorno.returnLbl = Lblreturn
        entorno.size = 1

        if self.parametros != None:
            for parametro in self.parametros:
                if parametro['tipo'] == 'struct':
                    simbolo = entorno.setTabla(parametro['id'], parametro['tipo'], True)
                elif not isinstance(parametro['tipo'], List):
                    simbolo = entorno.setTabla(parametro['id'], parametro['tipo'], (parametro['tipo'] == 'string' or parametro['tipo'] == 'array' or parametro['tipo'] == 'struct'))
                else:
                    simbolo = entorno.setTabla(parametro['id'], parametro['tipo'][0], True)
                    simbolo.setTipoAux(parametro['tipo'][1])
                    if parametro['tipo'][0] == 'struct':
                        struct = arbol.getStruct(parametro['tipo'][1])
                        simbolo.setParams(struct.getParams())
            
        
        generador.addBeginFunc(self.ide)

        for instruccion in self.instrucciones:
            value = instruccion.interpretar(arbol, entorno)
            if isinstance(value, Error):
                arbol.setError(value)
            if isinstance(value, Return):
                if value.getTrueLbl() == '':
                    generador.addComment('Resultado a retornar en la funcion')
                    generador.setStack('P',value.getValor())
                    generador.addGoto(entorno.returnLbl)
                    generador.addComment('Fin del resultado a retornar')
                else:
                    generador.addComment('Resultado a retornar en la funcion')
                    generador.putLabel(value.getTrueLbl())
                    generador.setStack('P', '1')
                    generador.addGoto(entorno.returnLbl)
                    generador.putLabel(value.getFalseLbl())
                    generador.setStack('P', '0')
                    generador.addGoto(entorno.returnLbl)
                    generador.addComment('Fin del resultado a retornar')

        generador.addGoto(Lblreturn)
        generador.putLabel(Lblreturn)

        generador.addComment(f'Fin de la compilacion de la funcion {self.ide}')
        generador.addEndFunc()
        generador.addSpace()
        return


    def getParams(self):
        return self.parametros

    def getTipo(self):
        return self.tipo

class Llamada(Abstract):

    def __init__(self, ide, parametros, fila, columna):
        self.ide = ide
        self.parametros = parametros
        self.trueLbl = ''
        self.falseLbl = ''
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        funcion = arbol.getFuncion(self.ide)

        if funcion != None:
            generador.addComment(f'Llamada a la funcion {self.ide}')
            paramValues = []
            temps = []
            size = tabla.size

            if self.parametros is not None:
                for parametros in self.parametros:
                    if isinstance(parametros, Llamada):
                        self.guardarTemps(generador, tabla, temps)
                        a = parametros.interpretar(arbol, tabla)
                        if isinstance(a, Error): return a
                        paramValues.append(a)
                        self.recuperarTemps(generador, tabla, temps)
                    else:
                        value = parametros.interpretar(arbol, tabla)
                        if isinstance(value, Error):
                            return value
                        paramValues.append(value)
                        temps.append(value.getValue())
            
            temp = generador.addTemp()

            generador.addExp(temp,'P',size+1, '+')
            aux = 0
            if len(funcion.getParams()) == len(paramValues):
                for param in paramValues:
                    if funcion.parametros[aux]['tipo'] == param.getTipo():
                        aux += 1
                        generador.setStack(temp,param.getValue())
                        if aux != len(paramValues):
                            generador.addExp(temp,temp,1,'+')
                    else:
                        generador.addComment(f'Fin de la llamada a la funcion {self.ide} por error, consulte la lista de errores')
                        return Error("Semantico", f"El tipo de dato de los parametros no coincide con la funcion {self.ide}", self.fila, self.columna)

            generador.newEnv(size)
            self.getFuncion(generator=generador) # Sirve para llamar a una funcion nativa
            generador.callFun(funcion.ide)
            generador.getStack(temp,'P')
            generador.retEnv(size)
            generador.addComment(f'Fin de la llamada a la funcion {self.ide}')
            generador.addSpace()
            if funcion.getTipo() != 'boolean':
                print("aqui esta el retorno")
                return Return2(temp, funcion.getTipo(), True)
            else:
                generador.addComment('Recuperacion de booleano')
                if self.trueLbl == '':
                    self.trueLbl = generador.newLabel()
                if self.falseLbl == '':
                    self.falseLbl = generador.newLabel()
                generador.addIf(temp,1,'==',self.trueLbl)
                generador.addGoto(self.falseLbl)
                ret = Return(temp, funcion.getTipo(), True)
                ret.trueLbl = self.trueLbl
                ret.falseLbl = self.falseLbl
                generador.addComment('Fin de recuperacion de booleano')
                return ret

    def guardarTemps(self, generador, tabla, tmp2):
        generador.addComment('Guardando temporales')
        tmp = generador.addTemp()
        for tmp1 in tmp2:
            generador.addExp(tmp, 'P', tabla.size, '+')
            generador.setStack(tmp, tmp1)
            tabla.size += 1
        generador.addComment('Fin de guardado de temporales')
    
    def recuperarTemps(self, generador, tabla, tmp2):
        generador.addComment('Recuperando temporales')
        tmp = generador.addTemp()
        for tmp1 in tmp2:
            tabla.size -= 1
            generador.addExp(tmp, 'P', tabla.size, '+')
            generador.getStack(tmp1, tmp)
        generador.addComment('Fin de recuperacion de temporales')

    def getFuncion(self, generator):
        if self.ide == 'length':
            generator.fLength()
        elif self.ide == 'trunc':
            generator.fTrunc()
        elif self.ide == 'float':
            generator.fFloat()
        elif self.ide == 'uppercase':
            generator.fUpperCase()
        elif self.ide == 'lowercase':
            generator.fLowerCase()
        return