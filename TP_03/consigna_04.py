"""
4. Implemente una clase “factura” que tenga un importe correspondiente al total de la factura pero
de acuerdo a la condición impositiva del cliente (IVA Responsable, IVA No Inscripto, IVA Exento)
genere facturas que indiquen tal condición.
"""

from abc import ABC, abstractmethod

# Producto abstracto
class Factura(ABC):
    def __init__(self, importe_total):
        self.importe_total = importe_total

    @abstractmethod
    def descripcion(self):
        pass

# Productos concretos
class FacturaIVAResponsable(Factura):
    def descripcion(self):
        return f"Factura IVA Responsable: {self.importe_total}"

class FacturaIVANoInscripto(Factura):
    def descripcion(self):
        return f"Factura IVA No Inscripto: {self.importe_total}"

class FacturaIVAExento(Factura):
    def descripcion(self):
        return f"Factura IVA Exento: {self.importe_total}"

# Clase Factory
class FacturaFactory:
    @staticmethod
    def crear_factura(tipo, importe_total):
        if tipo == 'IVA Responsable':
            return FacturaIVAResponsable(importe_total)
        elif tipo == 'IVA No Inscripto':
            return FacturaIVANoInscripto(importe_total)
        elif tipo == 'IVA Exento':
            return FacturaIVAExento(importe_total)
        else:
            raise ValueError("Tipo de condición impositiva desconocida")

# Cliente (main)
if __name__ == "__main__":
    tipo_condicion = 'IVA Responsable'
    importe_total = 10000

    factura = FacturaFactory.crear_factura(tipo_condicion, importe_total)
    print(factura.descripcion())

    # Ejemplo cambiando la condición impositiva
    tipo_condicion = 'IVA Exento'
    factura = FacturaFactory.crear_factura(tipo_condicion, importe_total)
    print(factura.descripcion())

    # Ejemplo cambiando la condición impositiva
    tipo_condicion = 'IVA No Inscripto'
    factura = FacturaFactory.crear_factura(tipo_condicion, importe_total)
    print(factura.descripcion())