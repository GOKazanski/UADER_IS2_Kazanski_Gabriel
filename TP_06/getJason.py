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
import json, sys


# ------------------------------------- Código viejo -----------------------------------------
# --------------------------------------------------------------------------------------------
def codigo_viejo():
    # Obtiene el nombre del archivo JSON del primer argumento de la línea de comandos
    jsonfile = sys.argv[1]

    # Obtiene la clave del JSON que se desea extraer del segundo argumento de la línea de comandos
    jsonkey = sys.argv[2]

    # Abre el archivo JSON en modo lectura ('r')
    with open(jsonfile, 'r') as myfile:
        # Lee todo el contenido del archivo y lo almacena en la variable 'data'
        data = myfile.read()

    # Convierte la cadena de texto 'data' en un diccionario de Python
    obj = json.loads(data)

    # Imprime el valor asociado a 'jsonkey' en el diccionario 'obj'
    print(str(obj[jsonkey]))


# -------------------------------------              -----------------------------------------
# --------------------------------------------------------------------------------------------
def main():
    reader_type = sys.argv[3]

    if reader_type == "viejo":
        codigo_viejo()


# ---------------------------------------- Main ----------------------------------------------
# --------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()