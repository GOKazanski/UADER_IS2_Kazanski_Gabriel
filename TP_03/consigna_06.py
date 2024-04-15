"""
6. Extienda el ejemplo del taller para prototipos de forma que genere 20 anidamientos y que la
carga simulada de procesamiento dure 2 segundos.
"""

import copy
import time
from typing import Optional

class ProcesoPesado:
    """
    Clase que simula un proceso pesado.
    """
    def __init__(self, nombre: str, nivel: int = 1, subproceso: Optional['ProcesoPesado'] = None):
        self.nombre = nombre
        self.nivel = nivel
        self.subproceso = subproceso
        self.simular_carga_pesada()

    def simular_carga_pesada(self):
        """
        Simula una carga de procesamiento que dura 2 segundos.
        Este método se llama durante la inicialización del objeto.
        """
        print(f"Iniciando carga pesada para {self.nombre} - Nivel {self.nivel}")
        time.sleep(2)  # Simula una tarea que tarda 2 segundos.
        print(f"Carga pesada completada para {self.nombre} - Nivel {self.nivel}")

    def clonar(self) -> 'ProcesoPesado':
        """
        Crea una copia profunda de este objeto, incluyendo sus subprocesos.
        """
        return copy.deepcopy(self)

    def __str__(self):
        return f"\n ProcesoPesado(nombre={self.nombre}, nivel={self.nivel}, subproceso={self.subproceso})"

# Crea el prototipo inicial.
prototipo = ProcesoPesado("Prototipo", 1)

# Realiza 20 anidamientos clonando el prototipo anterior.
ultimo_clon = prototipo
for i in range(2, 22):  # Comienza en 2 porque el prototipo inicial ya es el nivel 1.
    nuevo_clon = ultimo_clon.clonar()
    nuevo_clon.nivel = i
    nuevo_clon.nombre = f"Clon {i}"
    ultimo_clon.subproceso = nuevo_clon
    ultimo_clon = nuevo_clon

# Imprime el resultado del anidamiento.
print(prototipo)
