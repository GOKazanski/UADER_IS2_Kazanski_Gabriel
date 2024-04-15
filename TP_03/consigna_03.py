"""
3. Genere una clase donde se instancie una comida rápida “hamburguesa” que pueda ser entregada en
mostrador, retirada por el cliente o enviada por delivery. A los efectos prácticos bastará que la
clase imprima el método de entrega.
"""

from abc import ABC, abstractmethod

# Producto
class Hamburguesa:
    def __init__(self, entrega=""):
        self.metodo_entrega = entrega

    def __str__(self):
        return f"Hamburguesa entregada mediante: {self.metodo_entrega}"

# Builder Interface
class Builder(ABC):
    @abstractmethod
    def preparar_hamburguesa(self, metodo_entrega):
        pass

    @abstractmethod
    def obtener_resultado(self):
        pass

# ConcreteBuilder
class HamburguesaBuilder(Builder):
    def __init__(self):
        self.hamburguesa = None

    def preparar_hamburguesa(self, metodo_entrega):
        self.hamburguesa = Hamburguesa(metodo_entrega)

    def obtener_resultado(self):
        return self.hamburguesa

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_hamburguesa(self, metodo_entrega):
        self.builder.preparar_hamburguesa(metodo_entrega)
        return self.builder.obtener_resultado()

# Main
def main():
    builder = HamburguesaBuilder()
    director = Director(builder)

    hamburguesa_mostrador = director.construir_hamburguesa("en mostrador")
    print(hamburguesa_mostrador)

    hamburguesa_cliente = director.construir_hamburguesa("retirada por el cliente")
    print(hamburguesa_cliente)

    hamburguesa_delivery = director.construir_hamburguesa("enviada por delivery")
    print(hamburguesa_delivery)

if __name__ == "__main__":
    main()

