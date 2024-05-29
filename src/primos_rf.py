#!/usr/bin/python3
# Programa en Python para mostrar todos los números primos dentro de un intervalo
# Copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados.

import os

class Primes:
    """Clase para manejar operaciones relacionadas con números primos."""

    @staticmethod
    def compute(number):
        """Método estático que verifica si un número es primo.

        Args:
            number (int): El número a verificar.

        Returns:
            bool: True si el número es primo, False en caso contrario.
        """
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if (number % i) == 0:
                return False
        return True

def main():
    # Limpia la consola según el sistema operativo
    os.system("cls" if os.name == 'nt' else "clear")

    lower = 1  # Valor inicial del rango
    upper = 100  # Valor final del rango

    # Imprime la lista de números primos desde el valor inicial hasta el valor final
    print("Los números primos entre", lower, "y", upper, "son:")

    # Recorre cada número en el rango y verifica si es primo
    for num in range(lower, upper + 1):
        if Primes.compute(num):
            print(num)

if __name__ == "__main__":
    main()
