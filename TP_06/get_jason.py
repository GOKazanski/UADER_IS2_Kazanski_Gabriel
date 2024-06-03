# Archivo: getJason.py
# Versión: 1.1
# Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

"""
Este programa lee un archivo JSON y obtiene el valor asociado a una clave específica.
Implementa un patrón Singleton para asegurar una única instancia de la clase lectora
de JSON y maneja argumentos de línea de comandos de forma robusta.
"""

# Importa el módulo json para trabajar con datos JSON
# Importa el módulo sys para manejar los argumentos de la línea de comandos
import json
import sys

# ------------------------------------- Código viejo -----------------------------------------
# --------------------------------------------------------------------------------------------
def codigo_viejo():
    """
    Función que contiene el código original.
    Obtiene el nombre del archivo JSON del primer argumento de la línea de comandos.
    Obtiene la clave del JSON que se desea extraer del segundo argumento de la línea de comandos.
    Lee y parsea el contenido del archivo JSON.
    Imprime el valor asociado a la clave dada.
    """
    # Obtiene el nombre del archivo JSON del primer argumento de la línea de comandos
    jsonfile = sys.argv[1]

    # Obtiene la clave del JSON que se desea extraer del segundo argumento de la línea de comandos
    jsonkey = sys.argv[2]

    # Abre el archivo JSON en modo lectura ('r')
    with open(jsonfile, 'r', encoding='utf-8') as myfile:
        # Lee todo el contenido del archivo y lo almacena en la variable 'data'
        data = myfile.read()

    # Convierte la cadena de texto 'data' en un diccionario de Python
    obj = json.loads(data)

    # Imprime el valor asociado a 'jsonkey' en el diccionario 'obj'
    print(str(obj[jsonkey]))

# ------------------------------------- Singleton --------------------------------------------
# --------------------------------------------------------------------------------------------
class JSONReaderSingleton:
    """
    Clase Singleton para la lectura de archivos JSON.
    Asegura que solo exista una instancia de esta clase.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Método para controlar la creación de una única instancia.
        """
        if not cls._instance:
            cls._instance = super(JSONReaderSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def read_json(self, jsonfile, jsonkey):
        """
        Lee el archivo JSON y obtiene el valor asociado a la clave especificada.
        """
        try:
            with open(jsonfile, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
            obj = json.loads(data)
            print(str(obj[jsonkey]))
        except FileNotFoundError:
            print(f"Error: El archivo '{jsonfile}' no se encontró.")
        except KeyError:
            print(f"Error: La clave '{jsonkey}' no se encuentra en el archivo JSON.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no es un JSON válido.")

# ------------------------------------- Branching by abstraction -----------------------------
# --------------------------------------------------------------------------------------------
def main():
    """
    Función principal que maneja los argumentos de línea de comandos y la lógica del programa.
    """
    # Verifica si hay suficientes argumentos
    if len(sys.argv) < 2:
        print("Uso: getJason.py <archivo_json> <clave_json> [viejo|nuevo] [-v]")
        return

    # Manejo del argumento de versión
    if sys.argv[1] == '-v':
        print("Versión 1.1")
        return

    # Verifica si hay suficientes argumentos para la ejecución normal
    if len(sys.argv) < 4:
        print("Error: argumentos insuficientes.")
        print("Uso: getJason.py <archivo_json> <clave_json> [viejo|nuevo] | [-v]")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    reader_type = sys.argv[3]

    if reader_type == "viejo":
        codigo_viejo()
    elif reader_type == "nuevo":
        reader = JSONReaderSingleton()
        reader.read_json(jsonfile, jsonkey)
    else:
        print("Error: El tercer argumento debe ser 'viejo' o 'nuevo'.")

# ---------------------------------------- Main ----------------------------------------------
# --------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()



# ---------- Para consola
# python getJason.py -v

# python getJason.py sitedata.json token1 viejo

# python getJason.py sitedata.json token1 nuevo
