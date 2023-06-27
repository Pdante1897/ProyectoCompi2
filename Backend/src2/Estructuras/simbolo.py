class Simbolo():

    def __init__(self, ide, tipo, posicion, globalVar, inHeap):
        self.id = ide
        self.tipo = tipo
        self.pos = posicion
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.valor = None
        self.tipoAux = ''
        self.length = 0
        self.referencia = False
        self.params = None
    
    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.id
    def getPos(self):
        return self.pos
    def getInHeap(self):
        return self.inHeap
    
    def getParams(self):
        return self.params
    
    def setParams(self, params):
        self.params = params
    
    def setTipo(self, tipo):
        self.tipo = tipo
    def setId(self, id):
        self.id = id
    def setPos(self, pos):
        self.pos = pos
    def setInHeap(self, valor):
        self.inHeap = valor
    
    def setTipoAux(self, tipo):
        self.tipoAux = tipo

    def getTipoAux(self):
        return self.tipoAux

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length

    def setReferencia(self, ref):
        self.referencia = ref
        
    def getReferencia(self):
        return self.referencia
    
    def getvalor(self):
        return self.valor
    def setvalor(self, valor):
        self.valor = valor