from sujeto import Sujeto

class Alquiler(Sujeto):
    def __init__(self, estado=str):
        self.estado = estado

    def setEstado(self, estado):
        self.estado = estado
        self.notify()

    def getEstado(self):
        return self.estado

@property

def estado(self):
    return self.estado

@estado.setter

def estado(self, value):
    self.estado = value