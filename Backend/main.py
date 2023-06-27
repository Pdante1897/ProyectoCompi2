from ast import Dict, List
from src.Instrucciones.DeclaraA import DeclareArray
from src.Abstract.Abstracto import ObjectType
from flask import Flask , jsonify, request
import analizadores as analizador
from flask_cors import CORS
from sintact import correr
from sintact2 import traducir
from sintact3 import correr2 as arbolito

from analizadores import lexer
from src.Estructuras.tablasimbolos import TablaSimbolos
from src.Estructuras.arbol import Arbol
from src.Estructuras.Error import Error
import json
import sys
import graphviz as gv

sys.setrecursionlimit(10000000)


app = Flask(__name__)
CORS(app)
@app.route("/", methods=['GET'])
def main():
    return "hola mundo!"



@app.route("/analizar", methods=['POST'])
def analizar():
    data = request.get_json()
    entrada = str(data["codigo"])
    print(entrada)
    Ejecucion = correr(entrada)
    consola = Ejecucion.get('consola')
    tabla = Ejecucion.get('tabla')
    errores = Ejecucion.get('errores')
    saltos = consola.count('\n')
    data = {}
    data["consola"] = consola
    data["tablaSimbolos"] = tablas(tabla)
    data["tablaErrores"] = horrores(errores)
    data["dotAst"] = arbolito(entrada)
    json_data = json.dumps(data, indent=saltos)
    return json_data

@app.route("/compilar", methods=['POST'])
def compilar():
    data = request.get_json()
    entrada = str(data["codigo"])
    print(entrada)
    consola = traducir(entrada)
    saltos = consola.count('\n')
    print(consola)
    data = {}
    data["consola"] = consola
    json_data = json.dumps(data, indent=saltos)
    return json_data


def tablas(tabla):
    tablita = []
    for x in tabla:
        aux = tabla[x].getValor()
        tipo = tabla[x].getTipo()
        if tipo is ObjectType.STRUCT: tipo= "struct"
        fila = tabla[x].getFila()
        colum = tabla[x].getColumna()
        simbolo = {'id': str(x), 'valor': str(aux), 'tipo': tipo, 'entorno': 'global', 'fila': str(fila), 'columna': str(colum)} 
        tablita.append(simbolo)
    print(tablita)
    return tablita
#tablaErrores
def horrores(errores):
    listerrores = []
    id = 0
    for error in errores:
        id = id + 1
        if isinstance(error, Error):
            errorAux = {'id': id, 'tipo': error.tipo, 'descripcion': error.desc, 'fila': error.fila, 'columna': error.columna} 
            listerrores.append(errorAux)
    return listerrores