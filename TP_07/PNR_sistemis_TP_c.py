# *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* PNR_sistemis
#* Programa para procesar modelos dinámicos basado en el modelo de Putnam-Norden_Rayleigh
#*
#* UADER - FCyT
#* Ingeniería de Software II
#*
# *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
import matplotlib.pyplot as plt

# Función de esfuerzo acumulado (modelo de Putnam-Norden-Rayleigh)
def E_acum(K, a, t):
    return K * (1 - np.exp(-a * t**2))

# Función de esfuerzo instantáneo (derivada del esfuerzo acumulado)
def E_instant(K, a, t):
    return 2 * K * a * t * np.exp(-a * t**2)

# Datos del proyecto
K_nuevo = 72  # Esfuerzo total en persona-mes
duracion_proyecto = 12  # Duración del proyecto en meses
a_nuevo = 0.05  # Parámetro de ajuste del modelo (estimado)

# Generar puntos de tiempo para la duración del proyecto
t_proyecto = np.linspace(0, duracion_proyecto, 100)

# Calcular esfuerzo instantáneo y acumulado para el nuevo proyecto
E_instant_nuevo = E_instant(K_nuevo, a_nuevo, t_proyecto)
E_acum_nuevo = E_acum(K_nuevo, a_nuevo, t_proyecto)

# Graficar el esfuerzo instantáneo
plt.plot(t_proyecto, E_instant_nuevo, label=f'Esfuerzo instantáneo (K={K_nuevo} PM)', color='blue')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (persona-mes)')
plt.legend()
plt.title('Distribución del esfuerzo instantáneo en el tiempo')
plt.show()

# Graficar el esfuerzo acumulado
plt.plot(t_proyecto, E_acum_nuevo, label=f'Esfuerzo acumulado (K={K_nuevo} PM)', color='green')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo acumulado (persona-mes)')
plt.legend()
plt.title('Distribución del esfuerzo acumulado en el tiempo')
plt.show()

# Hallar el esfuerzo instantáneo máximo
t_max_esfuerzo = t_proyecto[np.argmax(E_instant_nuevo)]
max_esfuerzo_instantaneo = np.max(E_instant_nuevo)

print(f"El esfuerzo instantáneo máximo ocurre en el mes {t_max_esfuerzo:.2f}, con un esfuerzo de {max_esfuerzo_instantaneo:.2f} persona-mes.")
