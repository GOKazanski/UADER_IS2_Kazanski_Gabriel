import os
os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

#lower = 1 # lower: valor inicial
lower=int(input("Ingrese desde que valor: "))
#upper = 50 # upper: valor final
upper=int(input("Ingrese hasta que valor: "))

# imprime la lista de números primos desde el valor inicial hasta el valor final
print("\nLos números primos entre", lower, "y", upper, "son:")

# realiza un bucle for para recorrer cada uno de los números en el rango
for num in range(lower, upper + 1):
    # todos los números primos son mayores que 1

    if num > 1:# omite el número 1 porque no es primo

        # realiza otro bucle para encontrar divisores del número
        for i in range(2, num):

            # si el resto es cero, hay un divisor
            if (num % i) == 0:
                break
        else:
            print(num)
