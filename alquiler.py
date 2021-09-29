from sujeto import Sujeto

class Alquiler(Sujeto):
    def __init__(self, estado=str):
        self.estado = estado

    def setEstado(self, estado):
        self.estado = estado
        self.notify()

    def getEstado(self):
        return self.estado