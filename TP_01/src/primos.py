#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# lower: valor de comienzo
# upper: valor del final
lower = 1
upper = 100

# imprime el listado de numeros primos desde valor de comienzo hasta valor final
print("Prime numbers between", lower, "and", upper, "are:")

# realiza bucle for para recorrer cada uno de los numeros que hay en el rango
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1

    #ignora el numero 1 porque no es primo
    if num > 1:

        # realiza otro bucle para encontrar divisores del numero 
        for i in range(2, num):

            # si el resto es cero hay divisor
            if (num % i) == 0:
                break
        else:
            print(num)
