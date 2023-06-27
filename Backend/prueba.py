import ply.yacc as yacc
import ply.lex as lex
from analizadores import tokens
from analizadores import lexer, getColumna
import json

from src.Expresiones.Identificadores import Identificador
from src.Estructuras.arbol import Arbol
from src.Estructuras.Error import Error
from src.Expresiones.Aritmeticas import Aritmetica
from src.Expresiones.Primitivos import Primitivos
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Declarar_variables import Declaracion_Variables
from src.Estructuras.tablasimbolos import TablaSimbolos

precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIV','MOD'),
    ('left','EXP'),

    ('left','PARIZQ', 'PARDER'),
    ('right','UMENOS'),
    ('right','UNOT'),

)

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_evaluar(t):
    'instruccion : imprimir PTCOMA'
    t[0] = t[1]

def p_imprimir(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ expresion PARDER'
    t[0] = Imprimir(t[5], t.lineno(1), getColumna(input, t.slice[1]))

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion EXP expresion
                | expresion MOD expresion'''
    if t[2] == '+'  : 
        t[0] = Aritmetica(t[1], t[3], '+', t.lineno(2), getColumna(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], '-', t.lineno(2), getColumna(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmetica(t[1], t[3], '*', t.lineno(2), getColumna(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), getColumna(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmetica(t[1], t[3], '^', t.lineno(2), getColumna(input, t.slice[2]))
    elif t[2] == '%': 
        t[0] = Aritmetica(t[1], t[3], '%', t.lineno(2), getColumna(input, t.slice[2]))




def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    print(t[2])
    if t[1] == '-' : t[0] = Aritmetica(0, t[2], '-', t.lineno(1), getColumna(input, t.slice[1]))


def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos('number', int(t[1]), t.lineno(1), getColumna(input, t.slice[1]))


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos('number', float(t[1]), t.lineno(1), getColumna(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos('string', t[1], t.lineno(1), getColumna(input, t.slice[1]))

def p_expresion_true(t):
    'expresion : TRUE'
    t[0] = Primitivos('boolean', t[1], t.lineno(1), getColumna(input, t.slice[1]))

def p_expresion_false(t):
    'expresion : FALSE'
    t[0] = Primitivos('boolean', t[1], t.lineno(1), getColumna(input, t.slice[1]))


def p_expresion_parentecis(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_error(t):
    print(" Error sintáctico en '%s'" % t.value)

input = ''

def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

entrada = 'console.log(" 123123 " + true + false); console.log(" 123 " * true + false); console.log(" 123 " + true + false);'
def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

lexer.input(entrada)
test_lexer(lexer)
instrucciones = parse(entrada)
#arboljson=json.dumps(str(instrucciones))
#print(arboljson)
ast = Arbol(instrucciones)
tsg = TablaSimbolos()
ast.setTsglobal(tsg)


for instruccion in ast.getInstr():
    value = instruccion.interpretar(ast,tsg)
    if isinstance(value, Error):
        ast.getErrores().append(value)
        #ast.updateConsola(value.toString())
print(ast.getConsola())
