#!/usr/bin/python
# --------------------------------------------------------------------------------
# factorial.py
#
# Descripción:
# Este script calcula el factorial de un número entero no negativo proporcionado 
# como argumento de línea de comandos. El factorial de un número n (n!) es el 
# producto de todos los enteros positivos menores o iguales a n. Por definición,
# el factorial de 0 es 1. Este script es útil para entender conceptos básicos de 
# iteración y el uso de argumentos de línea de comandos en Python.
#
# Autor: Dr.P.E.Colla
# Año: 2022
# Licencia: Creative Commons
#
# Uso:
# Ejecute el script desde la línea de comandos pasando un número entero no negativo
# como argumento. Por ejemplo:
# ./factorial.py 5
# Esto calculará el factorial de 5, que es 120.
# --------------------------------------------------------------------------------

import sys

def factorial(num): 
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    num (int): El número entero del cual calcular el factorial.

    Retorna:
    int: El factorial del número dado. Si el número es negativo,
    se imprime un mensaje de error y no se retorna ningún valor.
    """
    if num < 0: 
        print("Factorial de un número negativo no existe.")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
    print("Debe informar un número!")
    sys.exit()

# Conversión del argumento de línea de comandos a entero y cálculo del factorial
num = int(sys.argv[1])
print(f"Factorial {num}! es {factorial(num)}")
