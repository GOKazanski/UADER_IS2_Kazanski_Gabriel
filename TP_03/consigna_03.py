"""
3. Genere una clase donde se instancie una comida rápida “hamburguesa” que pueda ser entregada en
mostrador, retirada por el cliente o enviada por delivery. A los efectos prácticos bastará que la
clase imprima el método de entrega.
"""

class Hamburguesa:
    """
    Esta clase representa una hamburguesa que puede ser entregada
    de diferentes maneras: en el mostrador, para llevar por el cliente,
    o mediante delivery.
    """

    def __init__(self, metodo_entrega="mostrador"):
        """
        Inicializa una nueva instancia de la hamburguesa con un método de entrega.

        :param metodo_entrega: El método de entrega inicial de la hamburguesa.
        """
        self.metodo_entrega = metodo_entrega

    def establecer_metodo_entrega(self, metodo_entrega):
        """
        Establece o cambia el método de entrega de la hamburguesa.

        :param metodo_entrega: El nuevo método de entrega para la hamburguesa.
        """
        self.metodo_entrega = metodo_entrega

    def imprimir_metodo_entrega(self):
        """
        Imprime el método de entrega de la hamburguesa.
        """
        print(f"El método de entrega de la hamburguesa es: {self.metodo_entrega}.")


# Creando una hamburguesa y especificando el método de entrega
hamburguesa1 = Hamburguesa("delivery")
hamburguesa1.imprimir_metodo_entrega()

# Creando otra hamburguesa con el método de entrega por defecto y luego cambiándolo
hamburguesa2 = Hamburguesa()
hamburguesa2.imprimir_metodo_entrega()  # Mostrará "mostrador" como método de entrega por defecto
hamburguesa2.establecer_metodo_entrega("para llevar")
hamburguesa2.imprimir_metodo_entrega()
