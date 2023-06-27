from src2.Estructuras.simbolo import Simbolo
from src.Estructuras.Error import Error


class TablaSimbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio la tabla esta vacia
        self.anterior = anterior # Apuntador al entorno anterior
        self.structs  = {}
        
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        self.recTemps = False
        self.size = 0
        if anterior != None:
            self.size = self.anterior.size

    def getTablaG(self):
        return self.tabla
    
    def setTabla(self, id, tipo, inHeap, find = True):
        if find:
            tablaActual = self
            while tablaActual != None:
                if id in tablaActual.tabla:
                    tablaActual.tabla[id].setTipo(tipo)
                    tablaActual.tabla[id].setInHeap(inHeap)
                    return tablaActual.tabla[id]
                else:
                    tablaActual = tablaActual.anterior
        if id in self.tabla:
            self.tabla[id].setTipo(tipo)
            self.tabla[id].setInHeap(inHeap)
            return self.tabla[id]
        else:
            simbolo = Simbolo(id,tipo,self.size,self.anterior == None, inHeap)
            self.size += 1
            self.tabla[id] = simbolo
            return self.tabla[id]
    
    
    def findTabla(self, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                return True
            else:
                tablaActual = tablaActual.anterior
        return False

    def setTablaFuncion(self, simbolo):
        self.tabla[simbolo.getId()] = simbolo
    
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
            if simbolo.getId() in tablaActual.tabla:
                tablaActual.tabla[simbolo.getId()].setvalor(simbolo.getvalor())
                tablaActual.tabla[simbolo.getId()].setTipo(simbolo.getTipo())
                return None
                # Si necesitan cambiar el tipo de dato
                # tablaActual.tabla[simbolo.getId()].setTipo(simbolo.getTipo())
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