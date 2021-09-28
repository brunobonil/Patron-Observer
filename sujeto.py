from observer import Observer

class  Sujeto():
    clientes = []

    def addCliente(self, cliente):
        print("Agregando cliente...")
        self.clientes.append(cliente)

    def removeClientes(self, cliente):
        print ("Quitando cliente...")
        self.clientes.remove(cliente)

    def notify(self):
        for i in self.clientes:
            i.update()