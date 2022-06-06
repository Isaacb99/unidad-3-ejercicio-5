from zope.interface import interface
from zope.interface import implementer

class Int(interface):
    
    def insertarElemento(self, elemento, posicion):
        pass
    def agregarElemento(self, elemento):
        pass
    def mostrarElemento(self, posicion):
        pass
