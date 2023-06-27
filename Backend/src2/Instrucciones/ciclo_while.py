
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones.Return import Return
from ..Estructuras.simbolo import Simbolo
from ..Abstract.Abstracto import Abstract
from ..Estructuras.tablasimbolos import Error
from ..Estructuras.arbol import Arbol
from ..Estructuras.tablasimbolos import TablaSimbolos
from ..Estructuras.generador import Generador


class While(Abstract):

    def __init__(self, condicion, bloqueWhile, fila, columna):
        self.condicion = condicion
        self.bloqueWhile = bloqueWhile
        super().__init__(fila, columna)
    
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        generador.addComment('Compilacion de un while')
        whileLabel = generador.newLabel()
        generador.putLabel(whileLabel)
        condicion = self.condicion.interpretar(arbol, tabla) # True o False
        if isinstance(condicion, Error) : return condicion
        if condicion.getTipo() == 'boolean':
            generador.putLabel(condicion.getTrueLbl())
            entorno = TablaSimbolos(tabla)  #NUEVO ENTORNO - HIJO - Vacio

            for instruccion in self.bloqueWhile:
                entorno.breakLbl = tabla.breakLbl
                entorno.continueLbl = tabla.continueLbl
                entorno.returnLbl = tabla.returnLbl
                result = instruccion.interpretar(arbol, entorno)
                if isinstance(result, Error):
                    arbol.setErrores(result)
                if isinstance(result, Break):
                    if tabla.breakLbl != '':
                        generador.addGoto(tabla.breakLbl)
                    else:
                        salir = generador.newLabel()
                        generador.addGoto(salir)
                        generador.putLabel(result.getLbl())
                        generador.putLabel(salir)
                        return Error("Semantico", "Sentencia break fuera de ciclo", self.fila, self.columna)
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
            
            generador.addGoto(whileLabel)
            generador.putLabel(condicion.getFalseLbl())

        generador.addComment('Fin de la compilacion de un while')