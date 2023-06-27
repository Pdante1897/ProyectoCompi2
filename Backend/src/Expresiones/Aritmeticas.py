from ..Instrucciones.AccesoA import AccessArray
from ..Expresiones.Primitivos import Primitivos
from ..Instrucciones.AccesoS import AccesoS
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        if isinstance(self.op_der, AccesoS):
            self.op_der = self.op_der.interpretar(arbol, tabla)
        if isinstance(self.op_izq, AccesoS):
            self.op_izq = self.op_izq.interpretar(arbol, tabla)
        
        if self.op_izq != 0: 
            izq = self.op_izq.interpretar(arbol, tabla)
            der = self.op_der.interpretar(arbol, tabla)
        else:
            izq = 0
            der = self.op_der.interpretar(arbol, tabla)
        if self.op == '-' and self.op_izq == 0:
            print("nice")
        elif self.op != '+' : 
            print(self.op)
            if self.op_izq.tipo != "number" or self.op_der.tipo != "number":
                return Error("Semantico", "Error, verificar las expresiones", self.fila, self.columna)
        if isinstance(self.op_der, AccessArray):
            valor = self.op_der.interpretar(arbol, tabla)
            if type(valor) == str: tipo = "string"
            elif type(valor) == int or type(valor) == float: tipo = "number"
            elif type(valor) == bool: tipo = "boolean"
            else: tipo = "any"
            self.op_der = Primitivos(tipo, valor, self.fila, self.columna)
        if isinstance(self.op_izq, AccessArray):
            valor = self.op_izq.interpretar(arbol, tabla)
            if type(valor) == str: tipo = "string"
            elif type(valor) == int or type(valor) == float: tipo = "number"
            elif type(valor) == bool: tipo = "boolean"
            else: tipo = "any"
            self.op_izq = Primitivos(tipo, valor, self.fila, self.columna)
        if self.op == '+':
            
            if self.op_izq.tipo == "number" and self.op_der.tipo == "string":
                izq = str(self.op_izq.interpretar(arbol, tabla))
                der = self.op_der.interpretar(arbol, tabla)
                self.tipo = 'string'
                
            elif self.op_izq.tipo == "string" and self.op_der.tipo == "number":
                izq = self.op_izq.interpretar(arbol, tabla)
                der = str(self.op_der.interpretar(arbol, tabla))
                self.tipo = 'string'
                
            elif self.op_izq.tipo == "string" and self.op_der.tipo == "string": 
                self.tipo = 'string'
            elif self.op_izq.tipo == "boolean" and self.op_der.tipo == "string": 
                self.tipo = 'string'
                izq = str(self.op_izq.interpretar(arbol, tabla))
            elif self.op_izq.tipo == "string" and self.op_der.tipo == "boolean": 
                self.tipo = 'string'
                der = str(self.op_der.interpretar(arbol, tabla))
            elif self.op_izq.tipo == "number" and self.op_der.tipo == "number": self.tipo = 'number'
            else: return Error("Semantico", "Error, verificar las expresiones", self.fila, self.columna)
            if isinstance(izq, Primitivos):
                izq = izq.valor
            if isinstance(izq, Primitivos):
                der = der.valor
            return izq + der
        elif self.op == '-':
            self.tipo = 'number'
            return izq - der
        elif self.op == '*':
            self.tipo = 'number'
            return izq * der
        elif self.op == '/':
            self.tipo = 'number'
            if der == 0:
                return 'Error: Division entre 0'
            return izq / der
        elif self.op == '^':
            self.tipo = 'number'
            return izq ** der
        elif self.op == '%':
            self.tipo = 'number'
            if der == 0:
                return 'Error: Division entre 0'
            return izq % der
        
    def getTipo(self):
        return self.tipo
