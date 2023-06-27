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
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generador = genAux.getInstance()
        temporal = ''
        operador = ''
                    
        if self.op_izq != 0: 
            izq = self.op_izq.interpretar(arbol, tabla)
            der = self.op_der.interpretar(arbol, tabla)
        else:
            izq = 0
            der = self.op_der.interpretar(arbol, tabla)
        if self.op == '-' and self.op_izq == 0:
            print("nice")
        
        if type(izq) is int or type(izq) is float: izq = Return(str(izq), "number", False)
        if type(der) is int or type(izq) is float: der = Return(str(der), "number", False)
        
        
        
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


