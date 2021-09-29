from observer import Observer


class Cliente(Observer):
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def setAlquiler(self, alquiler):
        self.alquiler = alquiler

    def update(self):
        print("Se ha actualizado el estado de los autos")
        print(f"Se le informa a {self.nombre} {self.apellido} con DNI: {self.dni} que el estado de su auto es: {self.alquiler.getEstado()}")

@property

def nombre(self):
    return self.nombre

@nombre.setter

def nombre(self, value):
    self.nombre = value

@property

def apellido(self):
    return self.apellido

@apellido.setter

def apellido(self, value):
    self.apellido = value

@property

def dni(self):
    return self.dni

@dni.setter

def dni(self, value):
    self.dni = value