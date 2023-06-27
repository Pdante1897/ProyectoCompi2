from abc import ABC, abstractmethod
from enum import Enum


class ObjectType(Enum):
    INTEGER = 1
    DECIMAL = 2
    BOOLEAN = 3
    STRING = 4
    ERROR = 5
    NULL = 6
    STRUCT = 7
    ARRAY = 8

class Abstract(ABC):
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    
    @abstractmethod
    def interpretar(self, arbol, tabla):
        pass