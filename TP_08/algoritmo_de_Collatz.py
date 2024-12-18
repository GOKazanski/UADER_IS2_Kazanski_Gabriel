#Calculando el número de iteraciones del algoritmo de Collatz

def collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones  # Se cambiado "iter" por "iteraciones"

# Comprobando los resultados
i = 2
print('El número de iteraciones para %d es %d\n' % (i, collatz(i)))  # Se cambiado "j" por "i"
