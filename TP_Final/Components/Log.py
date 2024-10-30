import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
import uuid
import datetime
from botocore.exceptions import ClientError

class Log:
    # Atributo de clase para almacenar la instancia Singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Asegura que solo haya una instancia de Log (implementación del patrón Singleton)."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa el recurso de DynamoDB y asigna la tabla CorporateLog."""
        self.dynamodb = boto3.resource('dynamodb')  # Conecta con DynamoDB en AWS
        self.table = self.dynamodb.Table('CorporateLog')  # Asigna la tabla 'CorporateLog'

    def post(self, uuid_session, method_name):
        """Registra un evento en la tabla CorporateLog de DynamoDB.

        Args:
            uuid_session (str): Identificador único de la sesión.
            method_name (str): Nombre del método que realiza la acción.

        El método crea un elemento de log con:
        - ID único (`id`)
        - ID de sesión (`session_id`)
        - ID de CPU (`CPUid`)
        - Nombre del método (`method`)
        - Marca de tiempo (`timestamp`)

        Si el registro tiene éxito, imprime un mensaje de confirmación; si falla, captura el error.
        """
        timestamp = datetime.datetime.now().isoformat()  # Marca de tiempo actual
        cpu_id = uuid.getnode()  # Obtiene un identificador único para la CPU
        unique_id = str(uuid.uuid4())  # Genera un identificador único para la entrada de log

        # Estructura del registro de log
        log_item = {
            'id': unique_id,            # Identificador único para la entrada
            'session_id': uuid_session,  # Identificador de la sesión
            'CPUid': cpu_id,             # Identificador de la CPU
            'method': method_name,       # Nombre del método que realiza la acción
            'timestamp': timestamp       # Marca de tiempo en formato ISO
        }

        try:
            # Inserta el log en la tabla CorporateLog
            self.table.put_item(Item=log_item)
            print(f"Operación registrada en el log: {log_item}")
        except botocore.exceptions.ClientError as e:
            # Captura y muestra un error si el registro falla
            print(f"Error al registrar en el log: {e.response['Error']['Message']}")

    def list(self, uuid_cpu, uuid=None):
        """Recupera entradas del log filtradas por el identificador de CPU y opcionalmente por sesión.

        Args:
            uuid_cpu (int): Identificador único de la CPU.
            uuid (str, opcional): Identificador único de la sesión para filtrar.

        Returns:
            list: Lista de entradas que coinciden con los filtros.

        Filtra los registros para incluir solo aquellos donde `CPUid` coincide con `uuid_cpu`.
        Si se proporciona `uuid`, filtra también por el identificador de sesión.
        Captura cualquier error y devuelve una lista vacía en caso de excepción.
        """
        try:
            # Filtra los registros donde 'CPUid' coincide con el uuid_cpu proporcionado
            response = self.table.scan(
                FilterExpression=Attr('CPUid').eq(uuid_cpu)
            )
            return response.get('Items', [])  # Devuelve las entradas encontradas
        except ClientError as e:
            # Captura y muestra el mensaje de error si falla la consulta
            print(e.response['Error']['Message'])
            return []
