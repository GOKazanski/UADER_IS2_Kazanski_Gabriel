import boto3
import botocore
from boto3.dynamodb.conditions import Attr
import uuid
import datetime
import logging
import json
from decimal import Decimal
from botocore.exceptions import ClientError

# Configuración del logger
logger = logging.getLogger('CorporateLogLogger')

# Función para habilitar el logger
def enable_logging():
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

class Log:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa el recurso de DynamoDB y la tabla 'CorporateLog'."""
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateLog')
        logger.debug("Instancia de Log inicializada con acceso a la tabla CorporateLog")

    def post(self, uuid_session, method_name):
        """Registra un evento en la tabla CorporateLog."""
        timestamp = datetime.datetime.now().isoformat()
        cpu_id = uuid.getnode()
        unique_id = str(uuid.uuid4())

        log_item = {
            'id': unique_id,
            'session_id': uuid_session,
            'CPUid': cpu_id,
            'method': method_name,
            'timestamp': timestamp
        }

        try:
            self.table.put_item(Item=log_item)
            logger.debug(f"Operación registrada en el log: {log_item}")
        except botocore.exceptions.ClientError as e:
            error_message = e.response['Error']['Message']
            logger.error(f"Error al registrar en el log: {error_message}")

    @staticmethod
    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

    def list(self, uuid_cpu, uuid=None):
        """Recupera una lista de elementos de la tabla CorporateLog, filtrando por CPUid."""
        try:
            filter_expression = Attr('CPUid').eq(uuid_cpu)
            if uuid:
                filter_expression &= Attr('session_id').eq(uuid)
            response = self.table.scan(FilterExpression=filter_expression)
            items = response.get('Items', [])

            logger.debug(f"{len(items)} entradas encontradas en CorporateLog para CPU {uuid_cpu}")
            return items  # Devuelve la lista de elementos encontrados
        except ClientError as e:
            error_message = e.response['Error']['Message']
            logger.error(f"Error al obtener los datos: {error_message}")
            return []
