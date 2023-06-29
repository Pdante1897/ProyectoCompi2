from ..Instrucciones.Funciones import Llamada
from ..Expresiones.Primitivos import Primitivos
from ..Instrucciones.AccesoS import AccesoS
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
from ..Abstract.retorno import Return
from ..Estructuras.generador import Generador

class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        genAux = Generador()
        generador = genAux.getInstance()
        temporal = ''
        operador = ''
        der = ''
        izq = self.op_izq.interpretar(tree, table)
        if isinstance(izq, Error): return izq
        if isinstance(self.op_der, Llamada):
            self.op_der.guardarTemps(generador, table, [izq.getValue()])
            der = self.op_der.interpretar(tree, table)
            if isinstance(der, Error): return der
            self.op_der.recuperarTemps(generador, table, [izq.getValue()])
        else:
            der = self.op_der.interpretar(tree, table)
            if isinstance(der, Error): return der

        if self.op == '+':
            operador = '+'
            temporal = generador.addTemp()
            generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
            self.tipo = 'number'
            return Return(temporal, self.tipo, True)
        elif self.op == '-':
            operador = '-'
            temporal = generador.addTemp()
            generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
            self.tipo = 'number'
            return Return(temporal, self.tipo, True)
        elif self.op == '*':
            operador = '*'
            temporal = generador.addTemp()
            generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
            self.tipo = 'number'
            return Return(temporal, self.tipo, True)
        elif self.op == '/':
            if der == 0:
                return 'Error: Division entre 0'
            operador = '/'
            temporal = generador.addTemp()
            generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
            self.tipo = 'number'
            return Return(temporal, self.tipo, True)
        elif self.op == '^':
            temporal = generador.addTemp()
            generador.addMathpow(temporal, izq.getValue(), der.getValue())
            self.tipo = 'number'            
            return Return(temporal, self.tipo, True)
        elif self.op == '%':
            if der == 0:
                return 'Error: Division entre 0'
            operador = '%'
            temporal = generador.addTemp()
            generador.addMathpow(temporal, izq.getValue(), der.getValue())
            self.tipo = 'number'            
            return Return(temporal, self.tipo, True)

    def getTipo(self):
        return self.tipo