import decimal
import math

from ..Estructuras.simbolo import Simbolo

from ..Expresiones.Identificadores import Identificador
from ..Expresiones.Aritmeticas import Aritmetica
from ..Abstract.Abstracto import Abstract
from ..Estructuras.Error import Error
import locale

class Nativa(Abstract):

    def __init__(self, expresion, nativa, parametros, fila, columna):
        self.expresion = expresion #
        self.nativa = nativa
        self.parametros = parametros
        self.valor = None # *
        self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        if not type(self.expresion) ==str:
            if isinstance(self.expresion, Simbolo): value = self.expresion.valor
            else: value = self.expresion.interpretar(arbol, tabla)
        else:
            self.expresion = tabla.getTabla(self.expresion)
            value = self.expresion.valor

        param = None
        if self.parametros is not None :
            for paramtero in self.parametros:
                if isinstance(paramtero, Identificador):
                    param = tabla.getTabla(paramtero.identificador)
                    break
                param = paramtero
                break
        if isinstance(value, Error):
            return value
        if self.nativa == "toFixed":
            if self.expresion.tipo != "number":
                return Error("Semantico", "Error, variable debe de ser tipo number", self.fila, self.columna)
            self.tipo = "number"
            return round(value, int(param.valor))
        elif self.nativa == "toExponential":
            if self.expresion.tipo != "number":
                return Error("Semantico", "Error, variable debe de ser tipo number", self.fila, self.columna)
            if isinstance(param, Aritmetica):
                self.tipo = "string"
                arit = param.interpretar(arbol, tabla)
                mantisa = value / (10 ** int(arit))
                return f"{round(mantisa, 3)}E{int(arit)}"
            mantisa = value / (10 ** int(param.valor))
            self.tipo = "string"
            return f"{round(mantisa, 3)}E{int(param.valor)}"
        elif self.nativa == "toString":
            self.tipo = "string"
            return str(value) 
        elif self.nativa == "toLowerCase":
            self.tipo = "string"
            return value.lower()
        elif self.nativa == "toUpperCase":
            self.tipo = "string"
            return value.upper()
        elif self.nativa == "split":
            return
        elif self.nativa == "concat":
            return
        elif self.nativa == "length":
            self.tipo = "number"
            return len(value.values)