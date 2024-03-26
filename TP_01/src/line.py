# Es para una visualización básica utilizando la biblioteca Matplotlib en Python. 
# Su propósito es ilustrar la relación entre un conjunto de valores para los ejes X e Y 
# mediante una línea que los conecta.

# Importación de las bibliotecas necesarias
import matplotlib.pyplot as plt  # Se utiliza para la creación de gráficos
import numpy as np  # Proporciona soporte para arrays y matrices, junto con una colección de funciones matemáticas para operar con estas estructuras

# Definición de los datos para los ejes
xaxis = np.array([0, 8])  # Array para el eje X
yaxis = np.array([4, 9])  # Array para el eje Y

# Creación del gráfico
plt.plot(xaxis, yaxis)  # Dibuja una línea entre los puntos definidos por los arrays xaxis y yaxis
plt.show()  # Muestra el gráfico
