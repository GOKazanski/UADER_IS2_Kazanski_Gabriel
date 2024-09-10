import numpy as np

# Definir variables
costo_mensual = 1000  # Inversión mensual en $
n_meses = 12  # Número de meses del proyecto
flujos_futuros = 18000  # Valor presente de los flujos futuros en el mes 12
tasa_efectiva_mensual = 0.01  # Tasa efectiva mensual

# Función para calcular el valor presente neto (VPN)
def calcular_vpn(costo_mensual, n_meses, flujos_futuros, tasa):
    # Valor presente de los costos mensuales
    valor_presente_costos = sum([costo_mensual / (1 + tasa)**t for t in range(1, n_meses+1)])
    # Valor presente de los flujos futuros
    valor_presente_futuros = flujos_futuros / (1 + tasa)**n_meses
    # Valor presente neto (VPN)
    vpn = valor_presente_futuros - valor_presente_costos
    return vpn, valor_presente_costos

# Calcular el VPN para el caso A (12 meses)
vpn_a, vp_inversion_a = calcular_vpn(costo_mensual, n_meses, flujos_futuros, tasa_efectiva_mensual)

# Calcular el VPN para el caso B (extensión de 3 meses)
vpn_b, vp_inversion_b = calcular_vpn(costo_mensual, n_meses + 3, flujos_futuros, tasa_efectiva_mensual)

# Calcular la rentabilidad en ambos casos (VPN sobre el valor presente de la inversión)
rentabilidad_a = vpn_a / vp_inversion_a
rentabilidad_b = vpn_b / vp_inversion_b

# Resultados
vpn_a, vp_inversion_a, rentabilidad_a, vpn_b, vp_inversion_b, rentabilidad_b
