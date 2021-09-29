from clientes import Cliente
from alquiler import Alquiler

def main():

    cliente1 = Cliente("Bruno", "Bonil", 42913529)

    alquiler1 = Alquiler()
    alquiler1.setEstado("No disponible")

    cliente1.setAlquiler(alquiler1)

    alquiler1.addCliente(cliente1)

    alquiler1.setEstado("Disponible")

    alquiler1.removeClientes(cliente1)
    alquiler1.setEstado("No Disponible")


if __name__ == "__main__":
    main()