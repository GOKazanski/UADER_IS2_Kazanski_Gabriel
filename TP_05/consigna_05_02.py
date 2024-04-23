"""
2. Implemente una clase bajo el patrón iterator que almacene una cadena de
caracteres y permita recorrerla en sentido directo y reverso.
"""
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List
import os

os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

class CharacterOrderIterator(Iterator):
    """
    El iterador concreto que permite recorrer una cadena de caracteres.
    """
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: StringCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> Any:
        if (0 <= self._position < len(self._collection)):
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            return value
        else:
            raise StopIteration()

class StringCollection(Iterable):
    """
    Una colección que almacena una cadena de caracteres y permite iterar sobre ella.
    """
    def __init__(self, text: str = "") -> None:
        self._collection = text

    def __iter__(self) -> CharacterOrderIterator:
        return CharacterOrderIterator(self._collection)

    def get_reverse_iterator(self) -> CharacterOrderIterator:
        return CharacterOrderIterator(self._collection, True)

    def add_char(self, char: str):
        self._collection += char

if __name__ == "__main__":
    # Creación de la colección con una cadena de caracteres inicial.
    cadena=input('Ingrese una palabra: ')
    collection = StringCollection(cadena)

    print("\nRecorrido directo:")
    for char in collection:
        print(char, end="")
    print("\n")

    print("Recorrido inverso:")
    for char in collection.get_reverse_iterator():
        print(char, end=" ")
    print()
