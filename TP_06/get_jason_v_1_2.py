# Archivo: obtener_json_v_1_2.py
# Versión: 1.2
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

"""
Este programa automatiza el proceso de selección de cuenta bancaria para pagos.
Implementa el patrón Singleton para obtener la clave de un token y el patrón de diseño
Chain of Responsibility para realizar pagos en cuentas balanceadas.
"""

import json
import sys
import os

# ----------------------------------- Clase de Manejo de Cuentas ----------------------------------
# -------------------------------------------------------------------------------------------------
class ManejadorCuentas:
    """
    Clase base para el manejo de cuentas bancarias.
    Implementa el patrón Chain of Responsibility.
    """

    def __init__(self, sucesor=None):
        """
        Inicializa el manejador de cuentas con un sucesor opcional.
        """
        self.sucesor = sucesor

    def manejar_solicitud(self, token_solicitud, monto_solicitud):
        """
        Maneja la solicitud de pago, delegando al sucesor si es necesario.
        token_solicitud: Token de la cuenta que intenta realizar el pago.
        monto_solicitud: Monto que se intenta pagar.
        return: El monto pagado si el manejo es exitoso, de lo contrario None.
        """
        if self.sucesor:
            return self.sucesor.manejar_solicitud(token_solicitud, monto_solicitud)
        return None

# ------------------------------------ Clase de Cuenta Bancaria -----------------------------------
# -------------------------------------------------------------------------------------------------
class CuentaBancaria(ManejadorCuentas):
    """
    Clase que representa una cuenta bancaria.
    """

    def __init__(self, token, saldo, sucesor=None):
        """
        Inicializa la cuenta bancaria con un token, un saldo y un sucesor opcional.
        token: Token de la cuenta bancaria.
        saldo: Saldo inicial de la cuenta bancaria.
        sucesor: Sucesor en la cadena de responsabilidad.
        """
        super().__init__(sucesor)
        self.token = token
        self.saldo = saldo

    def manejar_solicitud(self, token_solicitud, monto_solicitud):
        """
        Maneja la solicitud de pago si el token coincide y hay saldo suficiente.
        token_solicitud: Token de la cuenta que intenta realizar el pago.
        monto_solicitud: Monto que se intenta pagar.
        return: El monto pagado si el manejo es exitoso, de lo contrario delega al sucesor.
        """
        if token_solicitud == self.token and self.saldo >= monto_solicitud:
            self.saldo -= monto_solicitud
            print(f"Se realizó el pago desde la cuenta '{self.token}' por un monto de ${monto_solicitud}.")
            return monto_solicitud
        return super().manejar_solicitud(token_solicitud, monto_solicitud)

# --------------------------------------- Clase de Iterador ---------------------------------------
# -------------------------------------------------------------------------------------------------
class IteradorPagos:
    """
    Clase iteradora para manejar los pagos realizados.
    """

    def __init__(self):
        """
        Inicializa el iterador de pagos con una lista vacía de pagos.
        """
        self.pagos = []

    def agregar_pago(self, info_pago):
        """
        Agrega un pago a la lista de pagos.
        info_pago: Diccionario con la información del pago (token y monto).
        """
        self.pagos.append(info_pago)

    def listar_pagos(self):
        """
        Muestra todos los pagos realizados por orden cronológico.
        """
        for idx, pago in enumerate(self.pagos, start=1):
            print(f"Pedido N°: {idx}, Token: {pago['token']}, Monto: ${pago['monto']}")

# ------------------------------------------- Singleton -------------------------------------------
# -------------------------------------------------------------------------------------------------
class AdministradorTokensSingleton:
    """
    Clase Singleton para gestionar los tokens bancarios y sus claves.
    """
    _instancia = None

    def __new__(cls, *args, **kwargs):
        """
        Método para controlar la creación de una única instancia.
        """
        if not cls._instancia:
            cls._instancia = super(AdministradorTokensSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instancia.datos_token = {}
            cls._instancia.cargar_tokens()
        return cls._instancia

    def cargar_tokens(self):
        """
        Carga los tokens y sus claves desde el archivo JSON.
        """
        with open("sitedata.json", 'r', encoding='utf-8') as archivo:
            self.datos_token = json.load(archivo)

    def obtener_clave(self, token):
        """
        Obtiene la clave asociada a un token.
        token: Token de la cuenta bancaria.
        return: Clave asociada al token, o un mensaje si no se encuentra.
        """
        return self.datos_token.get(token, "Clave no encontrada")

# ---------------------------------------------- Main ---------------------------------------------
# -------------------------------------------------------------------------------------------------

def main():
    """
    Función principal del programa.
    Maneja la lógica de entrada de argumentos, creación de cuentas y procesamiento de pagos.
    """
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

    # Verifica si hay suficientes argumentos para la ejecución normal
    if len(sys.argv) < 4:
        if len(sys.argv) == 2 and sys.argv[1] in ["-v", "--version"]:
            print(sys.argv[0])
            print("Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.")
            print("Versión 1.2")
            print("\n")
            return
        else:
            print("Error: argumentos insuficientes.")
            print("Mostrar versión: [-v | --version]")
            print("Uso: <token1 = Saldo inicial > <token2 = Saldo inicial> <MONTO_PAGO = Valor del Pago>")
            print("\n")
            return

    try:
        token1_saldo = int(sys.argv[1])
        token2_saldo = int(sys.argv[2])
        MONTO_PAGO = int(sys.argv[3])
    except ValueError:
        print("Error: los argumentos deben ser enteros.")
        return

    # Carga de tokens y claves
    administrador_tokens = AdministradorTokensSingleton()

    # Creación de cuentas bancarias
    cuenta1 = CuentaBancaria("token1", token1_saldo)
    cuenta2 = CuentaBancaria("token2", token2_saldo)

    # Configuración del manejo de cuentas en cadena
    manejador_cuentas = ManejadorCuentas(cuenta1)
    cuenta1.sucesor = cuenta2

    # Manejo de solicitudes de pago
    iterador = IteradorPagos()

    # Realiza 10 pagos alternando entre dos tokens
    for i in range(1, 11):
        token_solicitud = f"token{i % 2 + 1}"
        monto_pagado = manejador_cuentas.manejar_solicitud(token_solicitud, MONTO_PAGO)
        if monto_pagado:
            iterador.agregar_pago({"token": token_solicitud, "monto": monto_pagado})

    # Listado de pagos realizados
    print("\nListado de pagos realizados:")
    iterador.listar_pagos()
    print("\n")

# ---------------------------------------------- Main ---------------------------------------------
# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# ---------- Ejecución desde consola ----------

# Para mostrar la versión:
# python get_jason_v_1_2.py -v
# python get_jason_v_1_2.py --version

# Para ejecutar el programa con argumentos:
# python get_jason_v_1_2.py 1000 2000 500
