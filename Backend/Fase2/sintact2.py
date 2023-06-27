from src2.Estructuras.generador import Generador
from src2.Instrucciones.AccesoS import AccesoS
from src2.Instrucciones.DeclaraS import DeclareStruct, CreaStruct, DeclareStruct2
from src2.Instrucciones.AsignaStruct import AsignaStruct
from src2.Instrucciones.Return import Return
from src2.Instrucciones.Nativas import Nativa
import ply.yacc as yacc
import ply.lex as lex
from analizadores2 import tokens
from analizadores2 import lexer, get_Columna, errores
from src2.Estructuras.Error import Error
from src2.Instrucciones.Imprimir import Imprimir, Imprimir2
from src2.Expresiones.Aritmeticas import Aritmetica
from src2.Expresiones.Primitivos import Primitivos
from src2.Expresiones.Identificadores import Identificador
from src2.Instrucciones.struct import Struct
from src2.Instrucciones.arrays import Arrays
from src2.Instrucciones.condicional_if import If
from src2.Instrucciones.ciclo_for import For
from src2.Instrucciones.ciclo_while import While
from src2.Expresiones.relacional_logica import Relacional_Logica
from src2.Instrucciones.Declarar_variables import Declaracion_Variables, Declaracion_Variables2, Declaracion_Variables3, Declaracion_Variables4
from src2.Instrucciones.Asignaciones import Asignacion_Variables, Asignacion_incrementable
from src2.Instrucciones.Funciones import Metodo, Llamada
from src2.Estructuras.tablasimbolos import TablaSimbolos
from src2.Estructuras.arbol import Arbol
from src2.Instrucciones.Typeof import TypeOf
from src2.Instrucciones.DeclaraA import DeclareArray
#from src2
#.Instrucciones.CreaS import CreaStruct


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
                  | declaracion_5
                  | condicional_ifs
                  | ciclo_for 
                  | ciclo_while
                  | asignaciones
                  | arrays_asigna
                  | expresionincr
                  | CONTINUE
                  | BREAK
                  | retorno'''
    t[0] = t[1]

def p_instrucciones_ciclo(t):
    '''instrucciones_ciclo : imprimir
                            | declaracion_1 
                            | declaracion_2
                            | declaracion_3
                            | declaracion_4
                            | declaracion_5
                            | condicional_ifs
                            | asignaciones
                            | expresion'''
    t[0] = t[1]

def p_imprimir(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ expresion PARDER'
    t[0] = Imprimir(t[5] , t.lineno(1), get_Columna(input, t.slice[1]))
def p_imprimir2(t):
    'imprimir : CONSOLE PUNTO LOG PARIZQ parametros PARDER'
    t[0] = Imprimir2(t[5] , t.lineno(1), get_Columna(input, t.slice[1]))


def p_declaracion_1(t):
    'declaracion_1 : LET ID DPUNTOS tipo IGUAL expresion'
    t[0] = Declaracion_Variables(t[2], t[4], t[6], t.lineno(1), get_Columna(input, t.slice[1]))

def p_declaracion_2(t):
    'declaracion_2 : LET ID DPUNTOS tipo'
    t[0] = Declaracion_Variables2(t[2], t[4], t.lineno(1), get_Columna(input, t.slice[1]))

def p_declaracion_3(t):
    'declaracion_3 : LET ID IGUAL expresion'
    t[0] = Declaracion_Variables3(t[2], t[4], t.lineno(1), get_Columna(input, t.slice[1]))

def p_declaracion_4(t):
    'declaracion_4 : LET ID OF expresion'
    t[0] = Declaracion_Variables3(t[2], t[4], t.lineno(1), get_Columna(input, t.slice[1]))

def p_declaracion_5(t):
    'declaracion_5 : LET ID'
    t[0] = Declaracion_Variables4(t[2], t.lineno(1), get_Columna(input, t.slice[1]))

#def p_declaracion_6(t):
    'declaracion_6 : LET expresion CORIZQ expresion CORDER'
    
    #t[0] = Declaracion_Variables(t[2], t[4], t[6], t.lineno(1), get_Columna(input, t.slice[1]))

#ME DA DUDA COMO FUNCIONAN LOS STRUCTS JAJA. PORQUE JALA LAS DECLARACIONES
#DENTRO DEL INTERFACE Y NO VEO QUE EXISTA

#*-----------------------------------------Crear Struct---------------------------------------------
def p_struct_(t):
    'struct : INTERFACE ID LLAIZQ parametros_struct LLADER'
    t[0] = CreaStruct(t[2], t[4] , t.lineno(1), get_Columna(input, t.slice[1]))

#def p_parametros_struct_(t):
#    'p_parametros_struct_ : expresion DPUNTOS expresion'



def p_parametrosStruct(t):
    'parametros_struct : parametros_struct parametro_struct'
    t[1].append(t[2])
    t[0] = t[1]

def p_parametrosStruct2(t):
    'parametros_struct : parametro_struct'
    t[0] = [t[1]]

def p_parametrosStruct3(t):
    '''parametro_struct : ID DPUNTOS tipo PTCOMA'''
    t[0] = {'tipo': str(t[3]), 'id': str(t[1]), 'valor': None}


#-----------------------------------------------Declarar Struct-----------------------------------------

def p_declareStruct(t):
    'declareStructST : LET ID DPUNTOS ID'
    t[0] = DeclareStruct(t[2], t[4], t.lineno(1), t.lexpos(1))


#------------------------------------------------Asignacion Structs--------------------------------------

def p_asignacionStructs(t):
    '''asignacionStructs : LET ID DPUNTOS ID IGUAL LLAIZQ parametros_structAsig LLADER 
                        | LET ID DPUNTOS ID IGUAL LLAIZQ parametros_structAsig COMA LLADER'''
    t[0] = DeclareStruct2(t[2], t[4], t[7], t.lineno(1), get_Columna(input, t.slice[1]))


def p_parametrosStructAsig(t):
    'parametros_structAsig : parametros_structAsig COMA parametro_structAsig '
    t[1].append(t[3])
    t[0] = t[1]

def p_parametrosStructAsig2(t):
    'parametros_structAsig : parametro_structAsig'
    t[0] = [t[1]]

def p_parametrosStructAsig3(t):
    '''parametro_structAsig : ID DPUNTOS expresion '''
    t[0] = {'expresion': t[3], 'id': t[1]}


#---------------------------------------------------Acceso Structs-----------------------------------------

def p_accesoStruct(t):
    'accesoStruct : ID PUNTO ID'
    t[0] = AccesoS(t[1], t[3], t.lineno(1), get_Columna(input, t.slice[1]))


#--------------------------------------------Asignacion por Acceso Structs-------------------------------------

def p_asignacionAccStruct(t):
    'asignacionAccStruct : ID PUNTO ID IGUAL expresion'
    t[0] = AsignaStruct(t[1], t[3], t[5], t.lineno(1), get_Columna(input, t.slice[1]))


#------------------------------------------------------Funciones-----------------------------------------------
def p_funciones(t):
    '''funciones : FUNCTION ID PARIZQ PARDER LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ  PARDER DPUNTOS tipo LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ parametrosfunc PARDER LLAIZQ instrucciones LLADER
                | FUNCTION ID PARIZQ parametrosfunc PARDER DPUNTOS tipo LLAIZQ instrucciones LLADER'''
    if len(t) == 8:
        t[0] = Metodo(t[2],None, t[6], t.lineno(1), get_Columna(input, t.slice[1]))
    elif len(t) == 10:
        t[0] = Metodo(t[2], None, t[8], t.lineno(1), get_Columna(input, t.slice[1]))
    elif len(t) == 9:
        t[0] = Metodo(t[2], t[4], t[7], t.lineno(1), get_Columna(input, t.slice[1]))
    else:
        t[0] = Metodo(t[2], t[4], t[9], t.lineno(1), get_Columna(input, t.slice[1]))

def p_funciones3_(t):
    'funciones : FUNCTION ID PARIZQ  PARDER LLAIZQ  LLADER'
    t[0] = Metodo(t[2], None, None, t.lineno(1), get_Columna(input, t.slice[1]))


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
                | ID'''
    if len(t) == 2:
        t[0] = {'tipo': 'any', 'id': t[1]}
    elif len(t) == 4:
        t[0] = {'tipo': t[3], 'id': t[1]}
    else:
        t[0] = {'tipo': t[4], 'id': t[2]}



def p_llamada(t):
    'llamada : ID PARIZQ  PARDER'
    t[0] = Llamada(t[1], None, t.lineno(1), get_Columna(input, t.slice[1]))
    

def p_llamada2(t):
    'llamada : ID PARIZQ parametros PARDER'
    if t[1] == "typeof":
        t[0] = TypeOf(t[3], t.lineno(1), get_Columna(input, t.slice[1]))

    else:
        t[0] = Llamada(t[1], t[3], t.lineno(1), get_Columna(input, t.slice[1]))


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
    t[0] = t[2]

def p_condicional_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = If(t[2], t[5], None, None, t.lineno(1), get_Columna(input, t.slice[1]))
    
    
def p_condicional_if_else(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER ELSE LLAIZQ instrucciones LLADER'
    t[0] = If(t[2], t[5], t[9], None, t.lineno(1), get_Columna(input, t.slice[1]))

def p_condicional_if_else_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAIZQ instrucciones LLADER ELSE IF condicional_if'
    t[0] = If(t[2], t[5], None, t[9], t.lineno(1), get_Columna(input, t.slice[1]))

def p_ciclo_for(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), get_Columna(input, t.slice[1]))
    
def p_ciclo_for2(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA expresionincr PARDER LLAIZQ instrucciones LLADER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), get_Columna(input, t.slice[1]))

def p_ciclo_for3(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA asignaciones PARDER LLAIZQ instrucciones LLADER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), get_Columna(input, t.slice[1]))

def p_ciclo_for4(t):
    'ciclo_for : FOR PARIZQ instrucciones_ciclo PTCOMA expresion PTCOMA asignaciones PARDER LLAIZQ  LLADER'
    #t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), get_Columna(input, t.slice[1]))

def p_ciclo_while(t):
    'ciclo_while : WHILE PARIZQ expresion PARDER LLAIZQ instrucciones LLADER'
    t[0] = While(t[3], t[6],  t.lineno(1), get_Columna(input, t.slice[1]))

def p_ciclo_while2(t):
    'ciclo_while : WHILE PARIZQ expresion PARDER LLAIZQ LLADER'
    t[0] = While(t[3], None,  t.lineno(1), get_Columna(input, t.slice[1]))
    
def p_arrays_asigna(t):
    '''arrays_asigna : CORIZQ expresion CORDER arrays_asigna
                 | IGUAL expresion'''
    if len(t) == 5:
        t[0]= Arrays(t[2],t.lineno(2), get_Columna(input, t.slice[2]))
    else:
        t[0] = (t[1], t[4],t.lineno(1), get_Columna(input, t.slice[1]))        

#def p_asignaciones_array(t):
#    '''asignaciones : ID CORIZQ expresion CORDER arrays_asigna
#                   | ID IGUAL expresion'''

def p_asignaciones_array(t):
    '''asignaciones : ID CORIZQ expresion CORDER arrays_asigna
                   | ID IGUAL expresion'''
    t[0] = Asignacion_Variables(t[1], t[3], t.lineno(1), get_Columna(input, t.slice[1]))



#---------------------------------------------Nativas----------------------------
def p_nativa(t):
    '''nativa : TOFIXED
                | TOSTRING
                | TOLOWERCASE
                | TOEXPONENTIAL
                | TOUPPERCASE
                | SPLIT
                | CONCAT'''
    t[0]=t[1]

def p_nativas(t):
    '''nativas : expresion PUNTO nativa PARIZQ parametros PARDER
              | ID PUNTO nativa PARIZQ  parametros PARDER'''
    t[0] = Nativa(t[1], t[3], t[5], t.lineno(2), get_Columna(input, t.slice[2]))

def p_nativas2(t):
    '''nativas : expresion PUNTO nativa PARIZQ  PARDER
                | ID PUNTO nativa PARIZQ  PARDER'''
    t[0] = Nativa(t[1], t[3], None, t.lineno(2), get_Columna(input, t.slice[2]))

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
    if t[2] == '+'  : 
        t[0] = Aritmetica(t[1], t[3], '+', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], '-', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmetica(t[1], t[3], '*', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '%': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '===':
        t[0] = Relacional_Logica(t[1], t[3], '===', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '!==':
        t[0] = Relacional_Logica(t[1], t[3], '!==', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional_Logica(t[1], t[3], '>', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional_Logica(t[1], t[3], '<', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional_Logica(t[1], t[3], '>=', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional_Logica(t[1], t[3], '<=', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Relacional_Logica(t[1], t[3], '&&', t.lineno(2), get_Columna(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Relacional_Logica(t[1], t[3], '||', t.lineno(2), get_Columna(input, t.slice[2]))

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    if t[1] == '-':
        print("aqui")
        t[0] = Aritmetica(0, t[2], '-', t.lineno(1), get_Columna(input, t.slice[1]))
        print("aqui2")

    elif t[1] == '!':
        t[0] = Relacional_Logica(t[2], None, '!', t.lineno(1), get_Columna(input, t.slice[1]))

def p_identificador(t):
    'expresion : ID'
    t[0] = Identificador(t[1], t.lineno(1), get_Columna(input, t.slice[1]), None)

def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos('number', int(t[1]), t.lineno(1), get_Columna(input, t.slice[1]))


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos('number', float(t[1]), t.lineno(1), get_Columna(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos('string', str(t[1]), t.lineno(1), get_Columna(input, t.slice[1]))
    #t[0] = t[1]
    
def p_expresion_true(t):
    'expresion : TRUE'
    t[0] = Primitivos('boolean', True, t.lineno(1), get_Columna(input, t.slice[1]))

def p_expresion_false(t):
    'expresion : FALSE'
    t[0] = Primitivos('boolean', False, t.lineno(1), get_Columna(input, t.slice[1]))

def p_expresion_null(t):
    'expresion : NULL'
    t[0]= Primitivos('any', 'null', t.lineno(1), get_Columna(input, t.slice[1]))
    
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
    if t[2] == '+':
        t[0] = Asignacion_incrementable(t[1], 1 , t.lineno(2), get_Columna(input, t.slice[2]) )
    else:
        t[0] = Asignacion_incrementable(t[1], -1 , t.lineno(2), get_Columna(input, t.slice[2]))
        
def p_expresion_parent(t):
    'expresion : PARIZQ expresion PARDER'
    #t[0] = DeclaraArray(t[2],  t.lineno(1), get_Columna(input, t.slice[1]))
    t[0] = t[2]

def p_expresion_array(t):
    'expresion : CORIZQ expresion CORDER'
    t[0]= t[2]
    





def p_retorno(t):
    '''retorno : RETURN expresion
                | RETURN'''
    if len(t) == 3:
        t[0] = Return(t[2], t.lineno(2), get_Columna(input, t.slice[1]) )
    else:
        t[0] = Return(None, t.lineno(1), get_Columna(input, t.slice[1]) )
        


def p_expression_error(t):
    '''instruccion : error 
                    | error instruccion'''
    t[0] = Error("Sintáctico", "Error Sintáctico:" + str(t[1].value), t.lineno(1), get_Columna(input, t.slice[1]))

    errores.append(
        errores.append(Error("Sintáctico", "Error Sintáctico:" + str(t[1].value), t.lineno(1), get_Columna(input, t.slice[1]))))

def p_error(t):
    errores.append(Error("Sintactico", "Error sintactico: " + str(t), 0, 0))
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
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

entradaP = 'interface estructura{Parametro: number; Parametro2:string;}'
def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def correr(entrada):
    lexer.input(entrada)
    test_lexer(lexer)
    instrucciones = parse(entrada)
    consola = ""

    ast = Arbol(instrucciones)
    tsg = TablaSimbolos()
    ast.setTsglobal(tsg)

    if True:
        for instruccion in ast.getInstr():
            if isinstance(instruccion, Metodo):
                ast.setFunciones(instruccion)
        
        for instruccion in ast.getInstr():
            if not(isinstance(instruccion, Metodo)):
                value = instruccion.interpretar(ast,tsg)
                if isinstance(value, Error):
                    ast.getErrores().append(value)
                    ast.updateConsola(value.toString())
            consola = ast.getConsola()
        #print(consola)
            
    return consola

#correr(entradaP)

def traducir(entrada):
    genAux = Generador()
    genAux.cleanAll(); # Limpia todos los archivos anteriores
    generador = genAux.getInstance()

    instrucciones = parse(entrada)
    ast = Arbol(instrucciones)
    tsg = TablaSimbolos()
    ast.setTsglobal(tsg)

    for instruccion in ast.getInstr():
        value = instruccion.interpretar(ast,tsg)
        if isinstance(value, Error):
            ast.setErrores(value)
    print(generador.getCode())  
