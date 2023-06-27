import graphviz


class Arbol:
    
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = {}
        self.errores = []
        self.consola = ""
        self.tsglobal = None
        self.tsgInterpretada = {}
    
    # Hacer los getters y setters de cada atributo

    def setTsgI(self, ambito, valor):
        self.tsgInterpretada[ambito] = valor
    
    def getTsgI(self):
        return self.tsgInterpretada # devolvemos el ambito global

    def getInstr(self):
        return self.instrucciones

    def setInstr(self, instrucciones):
        self.instrucciones = instrucciones
    
    def getFunciones(self):
        return self.funciones
    
    def setFunciones(self, id, function):
        if id in self.funciones.keys():
            return "error"
        else:
            self.funciones[id] = function

    def getFuncion(self, ide):
        actual = self
        if actual!=None:
            if ide in actual.funciones.keys():
                return actual.funciones[ide]
        return None
    
    def getErrores(self):
        return self.errores
    
    def setErrores(self, errores):
        self.errores.append(errores)
    
    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola
    
    def updateConsola(self, consola):
        self.consola += consola + '\n'
    
    def getTsglobal(self):
        return self.tsglobal

    def setTsglobal(self, tsglobal):
        self.tsglobal = tsglobal
    
    



class Nodo:
    def __init__(self, valor, tipo, id, nodos):
        self.valor = valor
        self.tipo = tipo
        self.id = id
        self.nodos = nodos if nodos is not None else []
    
    def agregarNodo(self, nodo):
        self.nodos.append(nodo)

    def getNodos(self):
        return self.nodos
    
    def generar_diagrama(self, dot):
        dot.node(str(self.id), f"{self.valor} ({self.tipo})")
        for nodo in self.nodos:
            dot.edge(str(self.id), str(nodo.id))
            nodo.generar_diagrama(dot)

    

# Crear la estructura de nodos
nodo1 = Nodo("Nodo 1", "Tipo 1", 1, None)
nodo2 = Nodo("Nodo 2", "Tipo 2", 2, None)
nodo3 = Nodo("Nodo 3", "Tipo 3", 3, None)

nodo4 = Nodo("Nodo 4", "Tipo 1", 4, None)
nodo5 = Nodo("Nodo 5", "Tipo 2", 5, None)
nodo6 = Nodo("Nodo 6", "Tipo 3", 6, None)
nodo7 = Nodo("Nodo 7", "Tipo 1", 7, None)
nodo8 = Nodo("Nodo 8", "Tipo 2", 8, None)
nodo9 = Nodo("Nodo 9", "Tipo 3", 9, None)

nodo1.agregarNodo(nodo2)
nodo1.agregarNodo(nodo3)

nodo2.agregarNodo(nodo4)
nodo2.agregarNodo(nodo5)

nodo3.agregarNodo(nodo6)

nodo5.agregarNodo(nodo7)
nodo5.agregarNodo(nodo8)
nodo5.agregarNodo(nodo9)



# Crear el objeto Graphviz
dot = graphviz.Digraph()

# Generar el diagrama
nodo1.generar_diagrama(dot)

print(dot)
# Renderizar y guardar el diagrama en un archivo
#dot.render('diagrama', format='png')