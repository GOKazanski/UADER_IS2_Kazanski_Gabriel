"""
3. Implemente una clase bajo el patrón observer donde una serie de clases están
subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4
caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio
coinciden. Implemente 4 clases de tal manera que cada una tenga un ID
especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con
ID para el que tenga una clase implementada.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import choices
from typing import List
import string
import os

os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

class Subject(ABC):
    """
    La interfaz Subject declara un conjunto de métodos para gestionar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjunta un observador al sujeto.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Desvincula un observador del sujeto.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a todos los observadores sobre un evento.
        """
        pass

class IDSubject(Subject):
    """
    El Subject posee algún estado importante y notifica a los observadores cuando este estado cambia.
    """

    _state: str = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Se ha adjuntado un observador con ID {observer.id}.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Subject: Se ha desvinculado un observador con ID {observer.id}.")

    def notify(self) -> None:
        print("Subject: Notificando a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def generate_id(self) -> None:
        self._state = ''.join(choices(string.ascii_uppercase + string.digits, k=4))
        print(f"\nSubject: Mi nuevo ID generado es: {self._state}")
        self.notify()

    def test_notifications(self) -> None:
        """
        Es una prueba de notificaciones utilizando los IDs de todos los observadores creados.
        """
        test_ids = ["A1B2", "C3D4", "E5F6", "G7H8"]
        for test_id in test_ids:
            self._state = test_id
            print(f"\nTest: Emitiendo ID de prueba {test_id}")
            self.notify()

class Observer(ABC):
    """
    La interfaz Observer declara el método de actualización, utilizado por los subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibe la actualización del subject.
        """
        pass

class SpecificIDObserver(Observer):
    def __init__(self, id: str):
        self.id = id

    def update(self, subject: Subject) -> None:
        if subject._state == self.id:
            print(f"{self.__class__.__name__}: Mi ID coincide ({self.id})!")

if __name__ == "__main__":
    # Código del cliente.

    subject = IDSubject()

    observers = [
        SpecificIDObserver("A1B2"),
        SpecificIDObserver("C3D4"),
        SpecificIDObserver("E5F6"),
        SpecificIDObserver("G7H8")
    ]

    print('--- Alta de observadores ---\n')
    for observer in observers:
        subject.attach(observer)

    print('\n--- Test de observadores ---')
    # Realizar la prueba de notificaciones
    subject.test_notifications()

    # Continuar con la generación aleatoria de IDs
    print('\n--- Creación de ID aleatorios ---')
    for _ in range(8):  # Genera 8 IDs
        subject.generate_id()

    print('\n--- Desvinculación de los observadores ---\n')
    for observer in observers:
        subject.detach(observer)
