# Importar librerías necesarias
from scipy.optimize import fsolve

# Datos iniciales
costo_mensual = 1000  # Costo mensual del proyecto
tasa_mensual = 0.01   # Tasa efectiva mensual del 1%
flujo_proyecto_final_12m = 18000  # Flujo de caja en el mes 12
flujo_proyecto_final_15m = 18000  # Mismo flujo de caja en el mes 15

# a) Valor Presente Neto (VPN) del proyecto en 12 meses
inversion_12_meses = [costo_mensual / (1 + tasa_mensual)**i for i in range(1, 13)]
vpn_12_meses = -sum(inversion_12_meses) + flujo_proyecto_final_12m / (1 + tasa_mensual)**12
valor_presente_inversion_12 = sum(inversion_12_meses)

print("a) Valor Presente Neto (12 meses):", round(vpn_12_meses, 2))

# b) VPN si el proyecto se extiende a 15 meses
inversion_15_meses = [costo_mensual / (1 + tasa_mensual)**i for i in range(1, 16)]
vpn_15_meses = -sum(inversion_15_meses) + flujo_proyecto_final_15m / (1 + tasa_mensual)**15
valor_presente_inversion_15 = sum(inversion_15_meses)

print("b) Valor Presente Neto (15 meses):", round(vpn_15_meses, 2))

# c) Rentabilidad en cada escenario
rentabilidad_12_meses = vpn_12_meses / valor_presente_inversion_12
rentabilidad_15_meses = vpn_15_meses / valor_presente_inversion_15

print("c) Rentabilidad (12 meses):", round(rentabilidad_12_meses * 100, 2), "%")
print("c) Rentabilidad (15 meses):", round(rentabilidad_15_meses * 100, 2), "%")

# d) Impacto financiero del retraso de 6 meses
print("d) Impacto del retraso: El retraso de 3 meses reduce el VPN y la rentabilidad debido a los costos adicionales y al descuento mayor sobre el flujo de caja futuro.")

# e) Impacto de contratar un gerente de proyecto (costo adicional del 5%)
costo_mensual_con_gerente = costo_mensual * 1.05
inversion_12_meses_con_gerente = [costo_mensual_con_gerente / (1 + tasa_mensual)**i for i in range(1, 13)]
vpn_12_meses_con_gerente = -sum(inversion_12_meses_con_gerente) + flujo_proyecto_final_12m / (1 + tasa_mensual)**12
valor_presente_inversion_12_con_gerente = sum(inversion_12_meses_con_gerente)
rentabilidad_12_meses_con_gerente = vpn_12_meses_con_gerente / valor_presente_inversion_12_con_gerente

print("e) VPN con gerente (12 meses):", round(vpn_12_meses_con_gerente, 2))
print("e) Rentabilidad con gerente (12 meses):", round(rentabilidad_12_meses_con_gerente * 100, 2), "%")

# f) Valor mensual máximo si el proyecto se extiende a 15 meses pero con el mismo VPN que 12 meses
def costo_mensual_max(costo):
    inversion_15_meses_con_costo = [costo / (1 + tasa_mensual)**i for i in range(1, 16)]
    vpn_con_costo = -sum(inversion_15_meses_con_costo) + flujo_proyecto_final_15m / (1 + tasa_mensual)**15
    return vpn_con_costo - vpn_12_meses  # Queremos que el VPN sea igual al de 12 meses

costo_max = fsolve(costo_mensual_max, costo_mensual)[0]

print("f) Valor mensual máximo aceptable (15 meses):", round(costo_max, 2))


# Ejercicio 19

# a) Pago ajustado si el patrocinante paga dos meses después
pago_mes_12 = 14000
pago_ajustado_mes_14 = pago_mes_12 * (1 + tasa_mensual)**2

print("19a) Pago ajustado (mes 14):", round(pago_ajustado_mes_14, 2))

# b) Pago ajustado si el proyecto termina en el mes 6 pero paga en el mes 12
pago_ajustado_mes_12_desde_mes_6 = pago_mes_12 / (1 + tasa_mensual)**6

print("19b) Pago ajustado (entrega mes 6, pago mes 12):", round(pago_ajustado_mes_12_desde_mes_6, 2))

# c) Pago ajustado si paga al finalizar el mes 6
pago_ajustado_mes_6 = pago_mes_12 / (1 + tasa_mensual)**6

print("19c) Pago ajustado (pago al finalizar mes 6):", round(pago_ajustado_mes_6, 2))
