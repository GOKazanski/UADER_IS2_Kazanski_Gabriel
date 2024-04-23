"""
1. Cree una clase bajo el patrón cadena de responsabilidad donde los números del
1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que
identifique la necesidad de consumir el número lo hará y caso contrario lo
pasará al siguiente en la cadena. Implemente una clase que consuma números
primos y otra números pares. Puede ocurrir que un número no sea consumido
por ninguna clase en cuyo caso se marcará como no consumido.
"""
import os
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import os

os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

class Handler(ABC):
    """
    La interfaz Handler declara un método para construir la cadena de manejadores.
    También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    El comportamiento de encadenamiento por defecto puede ser implementado dentro de una clase
    base de manejador.
    """

    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class PrimeHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if self.is_prime(request):
            return f"                   Primo: {request} es consumido"
        else:
            return super().handle(request)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


class EvenHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request % 2 == 0:
            return f"                                           Par: {request} es consumido"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    El código del cliente está diseñado para trabajar con una secuencia de números del 1 al 100
    y procesarlos a través de la cadena de manejadores configurada.
    """

    for number in range(1, 101):
        result = handler.handle(number)
        if result:
            print(result)
        else:
            print(f"{number} no fue consumido")


if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    # Configurar la cadena de responsabilidad
    prime_handler.set_next(even_handler)

    # Ejecutar el código del cliente
    print("Cadena: Primos > Pares\n")
    client_code(prime_handler)
    print("\n")

