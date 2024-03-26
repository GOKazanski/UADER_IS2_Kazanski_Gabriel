import matplotlib.pyplot as plt

def collatz(num):
    """
    Calcula la secuencia de Collatz para un número dado.

    Parámetros:
    - num (int): El número de inicio para la secuencia de Collatz.

    Retorna:
    - list: Una lista conteniendo la secuencia completa de Collatz para el número dado.
    """
    sequence_list = [num]  # Inicializa la lista de la secuencia con el número inicial.

    # Continúa calculando los términos de la secuencia hasta que llegue a 1.
    while num != 1:
        if num % 2 == 0:
            num = num // 2  # Si el número es par, divídelo entre 2.
        else:
            num = 3 * num + 1  # Si el número es impar, multiplícalo por 3 y suma 1.
        sequence_list.append(num)  # Añade el nuevo número a la secuencia.

    return sequence_list

# Prepara listas para almacenar los valores de x e y para el gráfico.
x_values = []
y_values = []

# Calcula la secuencia de Collatz para los números del 1 al 10,000.
for num in range(1, 10001):
    sequence_list = collatz(num)
    x_values.append(num)  # Almacena el número inicial en x_values.
    y_values.append(len(sequence_list))  # Almacena la longitud de la secuencia en y_values.

# Crea un gráfico de dispersión usando matplotlib.
plt.scatter(x_values, y_values, s=4)  # 's' ajusta el tamaño de los puntos en el gráfico.
plt.title("Longitud de las Secuencias de Collatz para los Primeros 10,000 Números Naturales")  # Añade un título al gráfico.
plt.xlabel("Número")  # Etiqueta para el eje x.
plt.ylabel("Longitud de la Secuencia")  # Etiqueta para el eje y.
plt.show()  # Muestra el gráfico.
