from src.Estructuras.Error import Error


class TablaSimbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio la tabla esta vacia
        self.anterior = anterior # Apuntador al entorno anterior
        self.structs  = {}
    
    def recorrer_tabla(self):
        # Recorrer la tabla hash e imprimir los elementos
        for clave, valor in self.tabla.items():
            print(f"Clave: {clave}, Valor: {valor}")

    def getTablaG(self):
        return self.tabla
    
    def setTabla(self, simbolo):
        # Aqui va la verificacion de que no se declare una variable dos veces
        self.tabla[simbolo.getID()] = simbolo
    
    def setTablaFuncion(self, simbolo):
        self.tabla[simbolo.getID()] = simbolo
    
    def getTabla(self, ide): # Aqui manejamos los entornos :3
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            else:
                tablaActual = tablaActual.anterior
        return None
    
    def updateTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.getID() in tablaActual.tabla:
                tablaActual.tabla[simbolo.getID()].setValor(simbolo.getValor())
                tablaActual.tabla[simbolo.getID()].setTipo(simbolo.getTipo())
                return None
                # Si necesitan cambiar el tipo de dato
                # tablaActual.tabla[simbolo.getID()].setTipo(simbolo.getTipo())
            else:
                tablaActual = tablaActual.anterior
        return Error("Semantico", "Variable no encontrada.", simbolo.getFila(), simbolo.getColumna())

    def GuardaStruct(self, id, atributo):
        if id in self.structs.keys():
            print("STRUCT YA CREADO")
        else:
            self.structs[id] = atributo
            
    def getStruct(self, id):
        ins = self
        while ins != None:  
            if id in ins.structs.keys():
                return ins.structs[id]
            print(id)
            ins = ins.anterior
        return None
    
    def updateTableStruct(self, simbolo):
        env = self
        while env is not None:
            if simbolo.ide in self.tabla.keys():
                env.tabla[simbolo.ide] = simbolo
                return
            env = env.anterior
        self.tabla[simbolo.ide] = simbolo