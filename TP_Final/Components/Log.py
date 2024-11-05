import boto3
import botocore
from boto3.dynamodb.conditions import Attr
import uuid as uuid
import datetime
import logging
import json
from decimal import Decimal
from botocore.exceptions import ClientError

# Configuración del logger
logger = logging.getLogger('CorporateLogLogger')
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
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateLog')

    def post(self, uuid_session, method_name):
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
            log_item_json = json.dumps(log_item, indent=2, ensure_ascii=False)
            logger.debug(f"Operación registrada en el log: {log_item_json}")
            print(f"Operación registrada en el log: {log_item_json}")
        except botocore.exceptions.ClientError as e:
            logger.error(f"Error al registrar en el log: {e.response['Error']['Message']}")

    @staticmethod
    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

    def list(self, uuid_cpu, uuid=None):
        try:
            response = self.table.scan(FilterExpression=Attr('CPUid').eq(uuid_cpu))
            items = response.get('Items', [])
            return items  # Devuelve siempre una lista
        except ClientError as e:
            logger.error(f'Error al obtener los datos:{e.response["Error"]["Message"]}')
            return []
