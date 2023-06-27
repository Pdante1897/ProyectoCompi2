
import ply.yacc as yacc
from analizadores import tokens
from analizadores import lexer, get_Columna, errores


#from src.Instrucciones.CreaS import CreaStruct


precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','UNOT','DIFQUE'),
    ('left','MENQUE','MAYQUE','MAYIGUALQUE','MENIGUALQUE'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV','MOD'),
    ('left','EXP'),
    ('left','PARIZQ', 'PARDER'),
    ('right','UMENOS'),
)

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccionpyc'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccionpyc'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccionpyc(t):
    '''instruccionpyc : instruccion PTCOMA
                  | instruccion''' 
    t[0] = t[1]

def p_instrucciones_evaluar(t):
    '''instruccion : imprimir 
                  | funciones
                  | llamada
                  | struct
                  | accesoStruct
                  | asignacionAccStruct
                  | declareStructST
                  | asignacionStructs
                  | declaracion_1 
                  | declaracion_2
                  | declaracion_3
                  | declaracion_4
                  | condicional_ifs
                  | ciclo_for 
                  | ciclo_while
                  | asignaciones
                  | arrays_asigna
                  | expresionincr
                  | prod_continue
                  | prod_break
                  | retorno'''
    t[0] = t[1]

def p_instrucciones_ciclo(t):
    '''instrucciones_ciclo : imprimir
                            | declaracion_1 
                            | declaracion_2
                            | declaracion_3
                            | declaracion_4
                            | condicional_ifs
                            | asignaciones
                            | expresion'''
    t[0] = t[1]

def p_imprimir(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ expresion PARDER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])

def p_imprimir2(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ parametros PARDER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])

def p_declaracion_1(t):
    'declaracion_1 : LET ID DPUNTOS tipo IGUAL expresion'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])

def p_declaracion_2(t):
    'declaracion_2 : LET ID DPUNTOS tipo'
    t[0] = (t[1], t[2], t[3], t[4])

def p_declaracion_3(t):
    'declaracion_3 : LET ID IGUAL expresion'
    t[0] = (t[1], t[2], t[3], t[4])

def p_declaracion_4(t):
    'declaracion_4 : LET ID'
    t[0] = (t[1], t[2])

def p_struct_(t):
    'struct : INTERFACE ID LLAIZQ parametros_struct LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5])

def p_parametrosStruct(t):
    'parametros_struct : parametros_struct parametro_struct'
    t[1].append(t[2])
    t[0] = (t[1])

def p_parametrosStruct2(t):
    'parametros_struct : parametro_struct'
    t[0] = [t[1]]

def p_parametrosStruct3(t):
    '''parametro_struct : ID DPUNTOS tipo PTCOMA'''
    t[0] = (t[1], t[2], t[3], t[4])

def p_declareStruct(t):
    'declareStructST : LET ID DPUNTOS ID'
    t[0] = (t[1], t[2], t[3], t[4])


#------------------------------------------------Asignacion Structs--------------------------------------

def p_asignacionStructs(t):
    '''asignacionStructs : LET ID DPUNTOS ID IGUAL LLAIZQ parametros_structAsig LLADER 
                        | LET ID DPUNTOS ID IGUAL LLAIZQ parametros_structAsig COMA LLADER'''
    if len(t) == 10: t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9])
    else: t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])


def p_parametrosStructAsig(t):
    'parametros_structAsig : parametros_structAsig COMA parametro_structAsig '
    t[1].append(t[3])
    t[0] = t[1]

def p_parametrosStructAsig2(t):
    'parametros_structAsig : parametro_structAsig'
    t[0] = [t[1]]

def p_parametrosStructAsig3(t):
    '''parametro_structAsig : ID DPUNTOS expresion '''
    t[0] = (t[1], t[2], t[3])

#---------------------------------------------------Acceso Structs-----------------------------------------

def p_accesoStruct(t):
    'accesoStruct : ID PUNTO ID'
    t[0] = (t[1], t[2], t[3])


#--------------------------------------------Asignacion por Acceso Structs-------------------------------------

def p_asignacionAccStruct(t):
    'asignacionAccStruct : ID PUNTO ID IGUAL expresion'
    t[0] = (t[1], t[2], t[3], t[4], t[5])


#------------------------------------------------------Funciones-----------------------------------------------
def p_funciones(t):
    '''funciones : FUNCTION ID PARIZQ PARDER LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ  PARDER DPUNTOS tipo LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ parametrosfunc PARDER LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ parametrosfunc PARDER DPUNTOS tipo LLAIZQ instrucciones LLADER'''
    if len(t) == 8:
        t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7])   
    elif len(t) == 10: 
        t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9])
    elif len(t) == 9:
        t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])
    else:
        t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])

def p_funciones3_(t):
    'funciones : FUNCTION ID PARIZQ  PARDER LLAIZQ  LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])


def p_parametrosf(t):
    'parametrosfunc : parametrosfunc COMA parametrofunc'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametrosf_2(t):
    'parametrosfunc : parametrofunc'
    t[0] = [t[1]]

def p_parametrof(t):
    '''parametrofunc : LET ID DPUNTOS tipo  
                | ID DPUNTOS tipo
                | ID DPUNTOS tipo CORIZQ CORDER
                | ID'''
    if len(t) == 2:
        t[0] = (t[1])
    elif len(t) == 4:
        t[0] = (t[1], t[2], t[3])
    elif len(t) == 6:
        t[0] = (t[1], t[2], t[3], t[4], t[5])
    else:
        t[0] = (t[1], t[2], t[3], t[4])



def p_llamada(t):
    'llamada : ID PARIZQ  PARDER'
    t[0] = (t[1], t[2], t[3])
    

def p_llamada2(t):
    'llamada : ID PARIZQ parametros PARDER'
    t[0] = (t[1], t[2], t[3], t[4])


def p_parametrosCall(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
def p_parametrosCall2(t):
    'parametros : parametro '
    t[0] = [t[1]]

def p_parametroCall(t):
    'parametro : expresion'
    t[0] = t[1]
#----------------------------------------------------------------------------Condicional IF------------------------------------------------------------------
def p_condicional_ifs(t):
    'condicional_ifs : IF condicional_if'
    t[0] = (t[1], t[2])

def p_condicional_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])
    
    
def p_condicional_if_else(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER ELSE LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])

def p_condicional_if_else_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER ELSE IF condicional_if'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9])

def p_ciclo_for(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11])    
def p_ciclo_for2(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA expresionincr PARDER LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11])    

def p_ciclo_for3(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA asignaciones PARDER LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11])    

def p_ciclo_for4(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA asignaciones PARDER LLAIZQ  LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])    

    
def p_ciclo_for5(t):
    '''ciclo_for : FOR PARIZQ LET ID OF expresion PARDER LLAIZQ instrucciones LLADER
                    | FOR PARIZQ LET ID OF ID PARDER LLAIZQ instrucciones LLADER'''
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])    




def p_ciclo_while(t):
    'ciclo_while : WHILE PARIZQ expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6], t[7])    

def p_ciclo_while2(t):
    'ciclo_while : WHILE PARIZQ expresion PARDER LLAIZQ LLADER'
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])    

    
def p_arrays_Declaracion(t):
    '''arrays_asigna : LET ID CORIZQ CORDER
                 | LET ID IGUAL CORIZQ parametros CORDER 
                 | CORIZQ parametros CORDER arrays_asigna
                 | IGUAL expresion'''
    if len(t) == 6:
        t[0] = (t[1], t[2], t[3], t[4], t[5])    
    elif len(t) == 5:
        t[0] = (t[1], t[2], t[3], t[4])    
    elif len(t) == 7:
        t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])    
    elif len(t) == 4:
        t[0] = (t[1], t[2], t[3])    

    else:
        t[0] = (t[1], t[2])    
    

def p_asignaciones_array(t):
    '''asignaciones : ID CORIZQ expresion CORDER arrays_asigna
                   | ID IGUAL expresion'''
    if len(t) == 6:
        t[0] = (t[1], t[2], t[3], t[4], t[5])  
    elif len(t) == 4:
        t[0] = (t[1], t[2], t[3])    

#---------------------------------------------Nativas----------------------------
def p_nativa(t):
    '''nativa : TOFIXED
                | TOSTRING
                | TOLOWERCASE
                | TOEXPONENTIAL
                | TOUPPERCASE
                | SPLIT
                | CONCAT
                | LENGTH'''
    t[0]=t[1]

def p_nativas(t):
    '''nativas : expresion PUNTO nativa PARIZQ parametros PARDER
              | ID PUNTO nativa PARIZQ  parametros PARDER'''
    t[0] = (t[1], t[2], t[3], t[4], t[5], t[6])    

def p_nativas2(t):
    '''nativas : expresion PUNTO nativa PARIZQ  PARDER
                | ID PUNTO nativa PARIZQ  PARDER'''
    t[0] = (t[1], t[2], t[3], t[4], t[5])    

#---------------------------------------------Tipos----------------------------
def p_tipo(t):
    '''tipo : STRING
            | NUMBER
            | BOOLEAN
            | ANY'''
    t[0] = t[1]

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion EXP expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | expresion IGUALQUE expresion
                | expresion DIFQUE expresion
                | expresion MAYQUE expresion
                | expresion MENQUE expresion
                | expresion MAYIGUALQUE expresion
                | expresion MENIGUALQUE expresion
                | expresion AND expresion
                | expresion OR expresion
                '''
    t[0] = (t[1], t[2], t[3])    



def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    t[0] = (t[1], t[2])    


def p_expresion_arr(t):
    'expresion : CORIZQ parametros CORDER'
    t[0] = (t[1], t[2], t[3])    

def p_expresion_array(t):
    '''expresion : ID CORIZQ expresion CORDER
                |  ID
    '''
    if len(t) == 2:
        t[0] = t[1]  
    else:
        t[0] = (t[1], t[2], t[3], t[4])    



def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = t[1]  


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]  

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = t[1]  
    
def p_expresion_true(t):
    'expresion : TRUE'
    t[0] = t[1]  

def p_expresion_false(t):
    'expresion : FALSE'
    t[0] = t[1]  

def p_expresion_null(t):
    'expresion : NULL'
    t[0] = t[1]  
    
def p_expresion_nativa(t):
    'expresion : nativas'
    t[0]=t[1]

def p_expresion_call(t):
    'expresion : llamada'
    t[0]=t[1]

def p_expresion_accesoStruct(t):
    'expresion : accesoStruct'
    t[0]=t[1]


def p_instruccion_incrementable(t):
    '''expresionincr : ID MAS MAS
                | ID MENOS MENOS'''
    t[0] = (t[1], t[2], t[3])    
        
def p_expresion_parent(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = (t[1], t[2], t[3])    

def p_expresion_array2(t):
    'expresion : CORIZQ expresion CORDER'
    t[0] = (t[1], t[2], t[3])    

    

def p_break(t):
    'prod_break : BREAK'
    t[0] = t[1]  

def p_continue(t):
    'prod_continue : CONTINUE'
    t[0] = t[1]  



def p_retorno(t):
    '''retorno : RETURN expresion
                | RETURN'''
    if len(t) == 3:
        t[0] = (t[1], t[2])    
    else:
        t[0] = t[1]  
        


def p_expression_error(t):
    '''instruccion : error 
                    | error instruccion'''
    

def p_error(t):
    print("Sintactico Error sintactico: " + str(t))
    if not t:
        return

    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()  # Get the next token
        print(tok)
        if not tok or tok.type == 'LLADER' or tok.type == 'PTCOMA':
            break
    parser.restart()





input = ''

def parse(inp):
    global parser

    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def correr2(entrada):
    lexer.input(entrada)
    test_lexer(lexer)
    instrucciones = parse(entrada)
    
    datos = generar_codigo_graphviz(instrucciones)

    return datos

#correr(entradaP)

import graphviz as gv




def generar_codigo_graphviz(arbol):
    codigo = '\n'
    contador_nodos = 0

    def agregar_nodo(valor, padre=None):
        nonlocal contador_nodos
        contador_nodos += 1
        nodo_id = 'n{}'.format(contador_nodos)
        codigo_nodo = '{} [label="{}"];\n'.format(nodo_id, valor)
        codigo_relacion = ''
        if padre:
            codigo_relacion = '{} -> {};\n'.format(padre, nodo_id)
        return nodo_id, codigo_nodo, codigo_relacion

    def recorrer_arbol(arbol, padre=None):
        nonlocal codigo
        if isinstance(arbol, tuple):
            valor = arbol[0]
            nodo_id, codigo_nodo, codigo_relacion = agregar_nodo(valor, padre)
            codigo += codigo_nodo
            codigo += codigo_relacion
            for hijo in arbol[1:]:
                recorrer_arbol(hijo, nodo_id)
        elif isinstance(arbol, list):
            for elemento in arbol:
                recorrer_arbol(elemento, padre)
        else:
            nodo_id, codigo_nodo, codigo_relacion = agregar_nodo(arbol, padre)
            codigo += codigo_nodo
            codigo += codigo_relacion

    # Agregar el nodo raíz "global"
    raiz_id, raiz_nodo, _ = agregar_nodo('global')
    codigo += raiz_nodo

    recorrer_arbol(arbol, raiz_id)
    return codigo

