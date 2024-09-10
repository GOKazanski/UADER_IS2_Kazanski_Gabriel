#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* PNR_sistemis
#* Programa para procesar modelos dinámicos basado en el modelo de Putman-Norden_Rayleigh
#*
#* UADER - FCyT
#* Ingeniería de Software II
#*
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Función de esfuerzo acumulado (modelo de Putnam-Norden-Rayleigh)
def E_acum(K, a, t):
    return K * (1 - np.exp(-a * t**2))

# Función de esfuerzo instantáneo (derivada del esfuerzo acumulado)
def E_instant(K, a, t):
    return 2 * K * a * t * np.exp(-a * t**2)

# Datos históricos (ejemplo)
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])        # Tiempo en meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11])  # Esfuerzo instantáneo en persona-mes

# Ajuste del modelo para los datos históricos
K_estimada = np.sum(E_data)  # Esfuerzo total del proyecto histórico
popt, _ = curve_fit(lambda t, a: E_instant(K_estimada, a, t), t_data, E_data, p0=[0.1])
a_estimada = popt[0]

# Definir el esfuerzo total del nuevo proyecto (72 PM en este caso)
K_nuevo = 72

# Generar puntos de tiempo para las curvas ajustadas
t_fit = np.linspace(min(t_data), max(t_data), 100)

# Esfuerzo instantáneo ajustado para los datos históricos
E_fit_hist = E_instant(K_estimada, a_estimada, t_fit)

# Esfuerzo instantáneo para el nuevo proyecto (72 PM)
E_fit_nuevo = E_instant(K_nuevo, a_estimada, t_fit)

# Graficar el esfuerzo instantáneo
plt.scatter(t_data, E_data, label='Datos históricos')
plt.plot(t_fit, E_fit_hist, label='Modelo ajustado (Histórico)', color='red')
plt.plot(t_fit, E_fit_nuevo, label=f'Nuevo proyecto (K={K_nuevo} PM)', color='blue')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (persona-mes)')
plt.legend()
plt.title('Distribución del esfuerzo en el tiempo')
plt.show()

# Esfuerzo acumulado ajustado para los datos históricos
E_acum_hist = E_acum(K_estimada, a_estimada, t_fit)

# Esfuerzo acumulado para el nuevo proyecto (72 PM)
E_acum_nuevo = E_acum(K_nuevo, a_estimada, t_fit)

# Graficar el esfuerzo acumulado
plt.plot(t_fit, E_acum_hist, label='Esfuerzo acumulado (Histórico)', color='red')
plt.plot(t_fit, E_acum_nuevo, label=f'Esfuerzo acumulado (K={K_nuevo} PM)', color='blue')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo acumulado (persona-mes)')
plt.legend()
plt.title('Esfuerzo acumulado en el tiempo')
plt.show()
