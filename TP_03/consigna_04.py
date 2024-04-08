"""
4. Implemente una clase “factura” que tenga un importe correspondiente al total de la factura pero
de acuerdo a la condición impositiva del cliente (IVA Responsable, IVA No Inscripto, IVA Exento)
genere facturas que indiquen tal condición.
"""

class Factura:
    """
    Clase base para facturas con un importe total.
    """

    def __init__(self, importe_total, condicion_impositiva):
        """
        Inicializa una nueva factura con un importe total y una condición impositiva.

        :param importe_total: El importe total de la factura.
        :param condicion_impositiva: La condición impositiva del cliente.
        """
        self.importe_total = importe_total
        self.condicion_impositiva = condicion_impositiva

    def imprimir_factura(self):
        """
        Imprime el importe total de la factura y la condición impositiva del cliente.
        """
        print(f"Importe total: {self.importe_total}, Condición impositiva: {self.condicion_impositiva}")


class IvaResponsable(Factura):
    """
    Factura para clientes con condición impositiva de IVA Responsable.
    """
    def __init__(self, importe_total):
        super().__init__(importe_total, "IVA Responsable")


class IvaNoInscripto(Factura):
    """
    Factura para clientes con condición impositiva de IVA No Inscripto.
    """
    def __init__(self, importe_total):
        super().__init__(importe_total, "IVA No Inscripto")


class IvaExento(Factura):
    """
    Factura para clientes con condición impositiva de IVA Exento.
    """
    def __init__(self, importe_total):
        super().__init__(importe_total, "IVA Exento")


# Uso de las clases
factura_responsable = IvaResponsable(1000)
factura_responsable.imprimir_factura()

factura_no_inscripto = IvaNoInscripto(2000)
factura_no_inscripto.imprimir_factura()

factura_exento = IvaExento(3000)
factura_exento.imprimir_factura()
