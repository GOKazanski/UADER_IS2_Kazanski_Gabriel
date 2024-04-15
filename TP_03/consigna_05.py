"""
5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar para construir
aviones en lugar de vehículos. Para simplificar suponga que un avión tiene un “body”, 2 turbinas,
2 alas y un tren de aterrizaje.
"""

from abc import ABC, abstractmethod

# Producto: Avión
class Avion:
    def __init__(self):
        self.body = ""
        self.turbinas = 0
        self.alas = 0
        self.tren_aterrizaje = ""

    def especificaciones(self):
        return (f"Avión con cuerpo {self.body}, "
                f"{self.turbinas} turbinas, "
                f"{self.alas} alas, "
                f"y tren de aterrizaje {self.tren_aterrizaje}.")

# Builder Interface
class Builder(ABC):
    @abstractmethod
    def construir_body(self, tipo):
        pass

    @abstractmethod
    def añadir_turbinas(self, cantidad):
        pass

    @abstractmethod
    def añadir_alas(self, cantidad):
        pass

    @abstractmethod
    def añadir_tren_aterrizaje(self, tipo):
        pass

    @abstractmethod
    def obtener_resultado(self):
        pass

# ConcreteBuilder
class AvionBuilder(Builder):
    def __init__(self):
        self.avion = Avion()

    def construir_body(self, tipo):
        self.avion.body = tipo
        return self

    def añadir_turbinas(self, cantidad):
        self.avion.turbinas = cantidad
        return self

    def añadir_alas(self, cantidad):
        self.avion.alas = cantidad
        return self

    def añadir_tren_aterrizaje(self, tipo):
        self.avion.tren_aterrizaje = tipo
        return self

    def obtener_resultado(self):
        return self.avion

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion(self, body, turbinas, alas, tren_aterrizaje):
        return self.builder.construir_body(body) \
            .añadir_turbinas(turbinas) \
            .añadir_alas(alas) \
            .añadir_tren_aterrizaje(tren_aterrizaje) \
            .obtener_resultado()

# Main
def main():
    builder = AvionBuilder()
    director = Director(builder)
    avion = director.construir_avion("comercial", 2, 2, "retráctil")
    print(avion.especificaciones())

if __name__ == "__main__":
    main()
