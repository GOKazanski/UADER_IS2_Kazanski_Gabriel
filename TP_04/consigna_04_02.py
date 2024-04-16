"""
2. Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
de 10 mts. Genere una clase que represente a las láminas en forma genérica al
cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
patrón bridge en la solución).

Con Bridge
"""
import os
from abc import ABC, abstractmethod

os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
class Laminador(ABC):
    """
    Define la interfaz para la implementación, que en este caso es cómo las láminas
    de acero son producidas.
    """
    @abstractmethod
    def producir_lamina(self, espesor, ancho):
        pass

class LaminadorCincoMetros(Laminador):
    """
    Implementación concreta del laminador que produce láminas de 5 metros de longitud.
    """
    def producir_lamina(self, espesor, ancho):
        return f"Lámina de {espesor}\" de espesor y {ancho}m de ancho y 5 metros de longitud producida."

class LaminadorDiezMetros(Laminador):
    """
    Implementación concreta del laminador que produce láminas de 10 metros de longitud.
    """
    def producir_lamina(self, espesor, ancho):
        return f"Lámina de {espesor}\" de espesor y {ancho}m de ancho y 10 metros de longitud producida."

class LaminaDeAcero:
    """
    Abstracción de lámina de acero que mantiene una referencia a un objeto Laminador,
    que realiza la implementación específica de la producción de la lámina.
    """
    def __init__(self, laminador: Laminador):
        self.laminador = laminador

    def producir(self, espesor, ancho):
        # Delega la operación a la implementación del laminador.
        return self.laminador.producir_lamina(espesor, ancho)

# Crear instancias de los laminadores
laminador_cinco_metros = LaminadorCincoMetros()
laminador_diez_metros = LaminadorDiezMetros()

# Crear una lámina de acero y decidir en tiempo de ejecución cuál laminador usar
lamina = LaminaDeAcero(laminador_cinco_metros)
print(lamina.producir(0.5, 1.5))
print('')

# Cambiar el laminador si es necesario
lamina.laminador = laminador_diez_metros
print(lamina.producir(0.5, 1.5))
print('')
