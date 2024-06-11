def collatz(n):

    if n <= 0:
        raise ValueError("El número debe ser mayor que 0")

    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

# Ejemplo de uso:
numero_inicial = int(input("Ingrese un numero: "))
iteraciones = collatz(numero_inicial)
print(f"El número de iteraciones necesarias para que {numero_inicial} alcance 1 es: {iteraciones}")
