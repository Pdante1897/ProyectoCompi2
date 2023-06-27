import ply.lex as lex
import ply.yacc  as yacc 
from src.Estructuras.Error import Error

errores = []

tokens   = [
#RESERVADAS
    'NUMBER',
    'STRING',
    'NULL',
    'ANY',
    'BOOLEAN',
    'LET',
    'INTERFACE',
    'FUNCTION',
    'CONSOLE',
    'LOG',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'OF',
    'BREAK',
    'CONTINUE',
    'RETURN',
#NATIVAS
    'TOFIXED',
    'TOEXPONENTIAL',
    'TOSTRING',
    'TOLOWERCASE',
    'TOUPPERCASE',
    'SPLIT',
    'CONCAT',
#CARACTERES Y CONECTORES
    'PUNTO',
    'PTCOMA',
    'COMA',
    'DPUNTOS',
    'LLAIZQ',
    'LLADER',
    'CORIZQ',
    'CORDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'MOD',
    'EXP',
    'MENQUE',
    'MAYQUE',
    'MENIGUALQUE',
    'MAYIGUALQUE',
    'IGUALQUE',
    'DIFQUE',
    'OR',
    'AND',
    'NOT',
    'TRUE',
    'FALSE',
#COMENTARIOS
    'COMENTMULTILINEA',
    'COMENTSIMPLE',
#NUMEROS
    'DECIMAL',
    'ENTERO',
#CADENAS
    'CADENA',
#IDENTIFICADORES
    'ID',
]

t_PUNTO    = r'\.'
t_PTCOMA    = r';'
t_COMA    = r','
t_DPUNTOS    = r':'
t_LLAIZQ   = r'{'
t_LLADER   = r'}'
t_CORIZQ   = r'\['
t_CORDER   = r']'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIV  = r'/'
t_MOD  = r'%'
t_EXP    = r'\^'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_MENIGUALQUE    = r'<='
t_MAYIGUALQUE    = r'>='
t_IGUALQUE  = r'==='
t_DIFQUE = r'!=='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'

#RESERVADAS

def t_NUMBER(t):
    r'number'
    return t
def t_STRING(t):
    r'string'
    return t
def t_NULL(t):
    r'null'
    return t
def t_ANY(t):
    r'any'
    return t
def t_BOOLEAN(t):
    r'boolean'
    return t
def t_LET(t):
    r'let'
    return t
def t_INTERFACE(t):
    r'interface'
    return t
def t_FUNCTION(t):
    r'function'
    return t
def t_CONSOLE(t):
    r'console'
    return t
def t_LOG(t):
    r'log'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_FOR(t):
    r'for'
    return t
def t_OF(t):
    r'of'
    return t
def t_BREAK(t):
    r'break'
    return t
def t_CONTINUE(t):
    r'continue'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_TRUE(t):
    r'true'
    return t
def t_FALSE(t):
    r'false'
    return t
#NATIVAS

def t_TOFIXED(t):
    r'toFixed'
    return t
def t_TOEXPONENTIAL(t):
    r'toExponential'
    return t
def t_TOSTRING(t):
    r'toString'
    return t
def t_TOLOWERCASE(t):
    r'toLowerCase'
    return t
def t_TOUPPERCASE(t):
    r'toUpperCase'
    return t
def t_SPLIT(t):
    r'split'
    return t
def t_CONCAT(t):
    r'concat'
    return t

# Comentario de múltiples líneas /* .. */
def t_COMENTMULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTSIMPLE(t):
    r'//.*(\n|$)'
    t.lexer.lineno += 1

def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    t.value = t.value
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = t.value
    return t

def t_CADENA(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Eliminar las comillas alrededor de la cadena
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

last_token_position = 0

def update_last_token_position(t):
    global last_token_position 

    last_token_position += 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    global last_token_position 
    last_token_position = 0

def get_Columna(inp, t):
    line_start = inp.rfind('\n', 0, t.lexpos) + 1
    return (t.lexpos - line_start) + 1

t_ignore = ' \r\t'

def t_error(t):
    errores.append(Error("Lexico", "Error Lexico" + t.value[0], t.lexer.lineno, get_Columna(input, t)))
    t.lexer.skip(1)


lexer = lex.lex()



#parsero = yacc .yacc()
