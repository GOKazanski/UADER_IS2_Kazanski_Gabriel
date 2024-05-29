# Importa el módulo json para trabajar con datos JSON
# Importa el módulo sys para manejar los argumentos de la línea de comandos
import json, sys

class JSONFileReader:
    _instance = None  # Variable de clase para almacenar la única instancia de la clase

    def __new__(cls, *args, **kwargs):
        # Si la instancia ya existe, retorna la instancia existente
        if cls._instance is None:
            cls._instance = super(JSONFileReader, cls).__new__(cls)
        return cls._instance

    def __init__(self, jsonfile):
        if not hasattr(self, 'initialized'):  # Verifica si ya ha sido inicializado
            self.jsonfile = jsonfile
            self.data = self._read_json_file()
            self.initialized = True

    def _read_json_file(self):
        # Abre el archivo JSON en modo lectura ('r')
        with open(self.jsonfile, 'r') as myfile:
            # Lee todo el contenido del archivo y lo almacena en la variable 'data'
            data = myfile.read()
        return json.loads(data)

    # devuelve el valor asociado a una clave específica en el JSON
    def get_value(self, jsonkey):
        return self.data.get(jsonkey, None)



# ----------------------- Main ---------------------------

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Si no se pasan o faltan argumentos
        print("Uso: python getJason.py <archivo_json> <clave_json>")
        sys.exit(1)

    # Obtiene el nombre del archivo JSON del primer argumento de la línea de comandos
    jsonfile = sys.argv[1]

    # Obtiene la clave del JSON que se desea extraer del segundo argumento de la línea de comandos
    jsonkey = sys.argv[2]

    # Creación de la instancia del lector de archivos JSON
    reader = JSONFileReader(jsonfile)

    # Obtención del valor asociado a la clave proporcionada
    value = reader.get_value(jsonkey)

    if value is not None:
        print(str(value)) # Imprime el valor asociado a 'jsonkey'
    else:
        # Sino encuentra el Token
        print(f"Clave '{jsonkey}' no encontrada en el archivo JSON.")
