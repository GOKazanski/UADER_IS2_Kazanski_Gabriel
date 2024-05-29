import random

# Función para generar una lista de números primos en un rango
def generar_primos(lower, upper):
    primos = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos

# Función para generar dos números primos al azar y multiplicarlos
def generar_clave(primos, historial):
    while True:
        p1, p2 = random.sample(primos, 2)
        par = (p1, p2)
        if par not in historial and (p2, p1) not in historial:
            historial.append(par)
            if len(historial) > 10:
                historial.pop(0)  # Elimina el par más antiguo si ya hay 10 pares en el historial
            return p1 * p2, historial

# Rango de números primos
lower = 1
upper = 100

# Generar lista de números primos
primos = generar_primos(lower, upper)

# Historial de los últimos 10 pares generados
historial = []

# Generar la clave de encriptación
clave, historial = generar_clave(primos, historial)
print("Clave de encriptación generada:", clave)
print("Historial de los últimos 10 pares:", historial)
