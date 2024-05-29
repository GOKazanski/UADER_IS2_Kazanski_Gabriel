#!/usr/bin/python3
# Python program to generate encryption keys using prime numbers
# copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados
import sys
import os
import random

#*---------------------------
#*--- Nueva clase primes
#*---------------------------
class ClassPrimes:
    def compute(self, numero_maximo):
        n = numero_maximo
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        else:
            return False

    def generate_primes(self, limit):
        primes = []
        for num in range(2, limit + 1):
            if self.compute(num):
                primes.append(num)
        return primes

#*------------------------------------------------------
#* Clase de abstracción
#*------------------------------------------------------
class BranchByAbstract:
    def __init__(self):
        self.generated_pairs = []

    def AbstractLayer(self, upper):
        primes = ClassPrimes().generate_primes(upper)
        print(f"Números primos entre 1 y {upper}: {primes}")

        while True:
            p1, p2 = random.sample(primes, 2)
            if (p1, p2) not in self.generated_pairs and (p2, p1) not in self.generated_pairs:
                self.generated_pairs.append((p1, p2))
                if len(self.generated_pairs) > 10:
                    self.generated_pairs.pop(0)
                break

        encryption_key = p1 * p2
        print(f"Números primos seleccionados: {p1}, {p2}")
        print(f"Clave de encriptación generada: {encryption_key}")
        print(f"Últimos 10 pares generados: {self.generated_pairs}")

#*------------------------------------------------------
#*------- Main del programa
#*------------------------------------------------------

os.system("clear")

print("Programa %s copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados" % (sys.argv[0]))

#*--- Define el límite superior para la generación de números primos
upper = 100

#*---- Crea la clase de abstracción
s1 = BranchByAbstract()

#*--- Ejecuta la generación de clave de encriptación
s1.AbstractLayer(upper)
