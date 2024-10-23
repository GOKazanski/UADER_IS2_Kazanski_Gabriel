import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

# Dataset histórico
data = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

# Inicialización del programa
version = "7.0"
linear = False
exponential = False
os.system('cls')

# Procesa argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--version", required=False, help="version", action="store_true")
ap.add_argument("-x", "--exponential", required=False, help="Exponential model", action="store_true")
ap.add_argument("-l", "--linear", required=False, help="Linear model", action="store_true")
args = vars(ap.parse_args())

if args['version'] == True:
    print("Program %s version %s" % (sys.argv[0], version))
    sys.exit(0)

if args['linear'] == True:
    print("Linear correlation model selected")
    linear = True

if args['exponential'] == True:
    print("Exponential correlation model selected")
    exponential = True

if linear == False and exponential == False:
    print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

# Dataset
df = pd.DataFrame(data)

# Función para calcular esfuerzo basado en modelo lineal
def predict_linear(loc):
    a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
    effort = a * loc + b
    return effort

# Función para calcular esfuerzo basado en modelo exponencial
def predict_exponential(loc):
    df['logEsfuerzo'] = np.log(df['Esfuerzo'])
    df['logLOC'] = np.log(df['LOC'])
    X = df['logLOC']
    Y = df['logEsfuerzo']
    X = sm.add_constant(X)
    mx = sm.OLS(Y, X).fit()
    k = np.exp(mx.params['const'])
    b = mx.params['logLOC']
    effort = k * (loc ** b)
    return effort

# Proceso modelo lineal
if linear == True:
    a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
    R = np.corrcoef(df['LOC'], df['Esfuerzo'], 1)
    R2 = R * R
    r_value = R2[1][0]

    print("Modelo lineal E=%.6f + %.6f*LOC)" % (b, a))
    print("El R-squared=%.4f (lineal)" % (r_value))

    plt.plot(df['LOC'], a * df['LOC'] + b, label=f'Modelo lineal (R^2={r_value:.2f})', color='red')

# Proceso modelo exponencial
if exponential == True:
    df['logEsfuerzo'] = np.log(df['Esfuerzo'])
    df['logLOC'] = np.log(df['LOC'])
    X = df['logLOC']
    Y = df['logEsfuerzo']
    X = sm.add_constant(X)

    mx = sm.OLS(Y, X).fit()
    print(mx.summary())

    k = np.exp(mx.params['const'])
    b = mx.params['logLOC']

    print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k, b))
    print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

    plt.plot(df['LOC'], k * (df['LOC'] ** b), label=f'Modelo exponencial (R^2={mx.rsquared:.2f})', color='green')

# Punto b: Predecir esfuerzo para LOC = 9100
loc_9100 = 9100
linear_pred_9100 = predict_linear(loc_9100)
exponential_pred_9100 = predict_exponential(loc_9100)

print(f"\nPredicción para LOC = {loc_9100}:")
print(f"Modelo lineal: {linear_pred_9100:.2f} persona-mes")
print(f"Modelo exponencial: {exponential_pred_9100:.2f} persona-mes")

# Punto c: Predecir esfuerzo para LOC = 200
loc_200 = 200
linear_pred_200 = predict_linear(loc_200)
exponential_pred_200 = predict_exponential(loc_200)

print(f"\nPredicción para LOC = {loc_200}:")
print(f"Modelo lineal: {linear_pred_200:.2f} persona-mes")
print(f"Modelo exponencial: {exponential_pred_200:.2f} persona-mes")

# Gráfico del dataset histórico
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos', color='blue')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()
