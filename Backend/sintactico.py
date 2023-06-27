import ply.yacc as yacc

from analizadores import lexer,tokens



precedence =(
    ('left','OR'),
    ('left','AND'),
    #('right','UNOT'),
    #('left','IGUALDAD','DIFERENTE'),
    #('left','MENOR','MENORIGUAL','MAYOR','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV','MOD'),
    #('right','POT'),
    ('left','PARIZQ','PARDER'),
    ('right','UMENOS'),
)


#Definicion de gramatica

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    
def p_instrucciones_lista(t):
    'instrucciones : instrucciones instruccion'
    if t[2] !="":
        t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0]=[t[1]]
        
def p_instrucciones_evaluar(t):
    '''instruccion : imprimir PTCOMA
    '''
    t[0]=[t[1]]
    
def p_imprimir(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ expresion PARDER'
    print(t[5])
    t[0]=t[5]
    
def p_expresion(t):
    ''' expresion : expresion MAS expresion
                     | expresion MENOS expresion
                     | expresion POR expresion       
                     | expresion DIV expresion
                     | expresion MOD expresion
                     | expresion POT expresion
                     | expresion MENOR expresion
                     | expresion MENORIGUAL expresion
                     | expresion MAYOR expresion 
                     | expresion MAYORIGUAL expresion
                     | expresion IGUALDAD expresion
                     | expresion DIFERENTE expresion
                     | expresion AND expresion
                     | expresion OR expresion
    '''
    if t[2] == '+'  : 
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*': 
        t[0] = t[1] * t[3]
    elif t[2] == '/': 
        t[0] = t[1] / t[3]
        
        
def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = int(t[1])

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = float(t[1])
    

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = t[1]

def p_error(t):
    print(" Error sintáctico en '%s'" % t.value)
    
def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)


entrada = 'console.log(3*5-4*2);'
def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

# lexer.input(entrada)
# test_lexer(lexer)
instrucciones = parse(entrada)