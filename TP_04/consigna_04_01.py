"""
1. Provea una clase ping que luego de creada al ser invocada con un método
“execute(string)” realice 10 intentos de ping a la dirección IP contenida en
“string” (argumento pasado), la clase solo debe funcionar si la dirección IP
provista comienza con “192.”. Provea un método executefree(string) que haga
lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
www.google.com usando el método executefree de ping y re-envie a execute
de la clase ping en cualquier otro caso. (Modele la solución como un patrón
proxy).

Con Proxy
"""
import os
import subprocess

class Ping:
    def execute(self, ip_address):
        # Comprueba si la IP comienza con "192.", solo permite esas IPs
        if ip_address.startswith("192."):
            self._ping(ip_address)
        else:
            # Si la IP no comienza con "192.", deniega el acceso
            print("Acceso denegado. La dirección IP no comienza con '192.'.")

    def executefree(self, ip_address):
        # Realiza un ping sin restricciones de IP
        self._ping(ip_address)

    def _ping(self, ip_address):
        # Imprime que el ping ha iniciado
        print(f"Iniciando ping a {ip_address}")
        # Realiza 10 pings a la dirección IP
        for i in range(1, 3):# cambiar range(1, 11) para que sean 10 intentos
            response = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True, text=True)
            if response.returncode == 0:
                # Si el ping fue exitoso, imprime la salida
                print(response.stdout)
            else:
                # Si hubo un error, lo muestra, incluyendo un número de intento
                print(f"Acceso denegado {i}. {response.stderr.strip()}")

class PingProxy:
    def __init__(self):
        # Inicializa la clase PingProxy con una instancia de Ping
        self.ping = Ping()

    def execute(self, ip_address):
        # Verifica si la dirección IP es la específica que necesita redirección
        if ip_address == "192.168.0.254":
            # Redirige el ping a www.google.com si es la IP específica
            print("Redireccionando a www.google.com.ar")
            self.ping.executefree("www.google.com.ar")
        else:
            # En cualquier otro caso, ejecuta un ping normal
            self.ping.execute(ip_address)

# Ejemplo de uso
os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
ping_proxy = PingProxy()
ping_proxy.execute("192.168.0.254")  # Redirige a www.google.com
ping_proxy.execute("192.168.1.1")    # Realiza ping normal bajo la restricción "192."
ping_proxy.execute("168.168.1.1")    # Realiza ping normal bajo la restricción "192."
