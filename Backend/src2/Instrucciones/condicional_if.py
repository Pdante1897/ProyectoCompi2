
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Estructuras.tablasimbolos import TablaSimbolos
from ..Estructuras.generador import Generador

class If(Abstract):

    def __init__(self, condicion, bloqueIf, bloqueElse, bloqueElseif, fila, columna):
        self.condicion = condicion
        self.bloqueIf = bloqueIf
        self.bloqueElse = bloqueElse
        self.bloqueElseif = bloqueElseif
        super().__init__(fila, columna)
    

    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment('Compilacion de un if')
        condicion = self.condicion.interpretar(arbol, tabla) # True o False
        if isinstance(condicion, Error) : return condicion

        if condicion.getTipo() == 'boolean':
            generador.putLabel(condicion.getTrueLbl())
            entorno = TablaSimbolos(tabla)  #NUEVO ENTORNO - HIJO - Vacio
            for instruccion in self.bloqueIf:
                entorno.breakLbl = tabla.breakLbl
                entorno.continueLbl = tabla.continueLbl
                entorno.returnLbl = tabla.returnLbl
                result = instruccion.interpretar(arbol, entorno)
                if isinstance(result, Error):
                    arbol.setErrores(result)
                # if isinstance(result, Break):
                #     if tabla.breakLbl != '':
                #         generador.addGoto(tabla.breakLbl)
                #     else:
                #         salir = generador.newLabel()
                #         generador.addGoto(salir)
                #         generador.putLabel(result.getLbl())
                #         generador.putLabel(salir)
                #         return Error("Semantico", "Sentencia break fuera de ciclo", self.fila, self.columna)
                if isinstance(result, Return):
                    if entorno.returnLbl != '':
                        generador.addComment('Resultado a retornar en la funcion')
                        if result.getTrueLbl() == '':
                            generador.setStack('P', result.getValor())
                            generador.addGoto(entorno.returnLbl)
                            generador.addComment('Fin del resultado a retornar en la funcion')
                        else:
                            generador.putLabel(result.getTrueLbl())
                            generador.setStack('P', '1')
                            generador.addGoto(entorno.returnLbl)
                            generador.putLabel(result.getFalseLbl())
                            generador.setStack('P', '0')
                            generador.addGoto(entorno.returnLbl)
                        generador.addComment('Fin del resultado a retornar en la funcion')

            salir = generador.newLabel()
            generador.addGoto(salir)
            generador.putLabel(condicion.getFalseLbl())

            if self.bloqueElse != None:
                entorno = TablaSimbolos(tabla)  #NUEVO ENTORNO - HIJO - Vacio
                for instruccion in self.bloqueElse:
                    entorno.breakLbl = tabla.breakLbl
                    entorno.continueLbl = tabla.continueLbl
                    entorno.returnLbl = tabla.returnLbl
                    result = instruccion.interpretar(arbol, entorno)
                    if isinstance(result, Error):
                        arbol.setErrores(result)
                    if isinstance(result, Return):
                        generador.addComment('Resultado a retornar en la funcion')
                        if result.getTrueLbl() == '':
                            generador.setStack('P', result.getValor())
                            generador.addGoto(entorno.returnLbl)
                            generador.addComment('Fin del resultado a retornar en la funcion')
                        else:
                            generador.putLabel(result.getTrueLbl())
                            generador.setStack('P', '1')
                            generador.addGoto(entorno.returnLbl)
                            generador.putLabel(result.getFalseLbl())
                            generador.setStack('P', '0')
                            generador.addGoto(entorno.returnLbl)
                        generador.addComment('Fin del resultado a retornar en la funcion')
            elif self.bloqueElseif != None:
                result = self.bloqueElseif.interpretar(arbol, tabla)
                if isinstance(result, Error): return result
            generador.putLabel(salir)
        generador.addComment('Fin de la compilacion de un if')