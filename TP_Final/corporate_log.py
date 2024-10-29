import boto3
import json
import uuid  # Asegura que uuid esté importado
from datetime import datetime
from boto3.dynamodb.conditions import Key

# Cargar credenciales AWS desde el archivo JSON
with open("IS2_TPFI_credentials.json") as cred_file:
    creds = json.load(cred_file)
aws_access_key = creds["accesskey"]
aws_secret_key = creds["secretkey"]
region = creds["region"]

class CorporateLog:
    _instance = None  # Atributo de clase para almacenar la instancia Singleton

    def __new__(cls):
        if cls._instance is None:
            # Crear una nueva instancia si no existe y configurarla para usar DynamoDB
            cls._instance = super(CorporateLog, cls).__new__(cls)
            cls._instance.dynamodb = boto3.resource(
                'dynamodb',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=region
            )
            cls._instance.table = cls._instance.dynamodb.Table('CorporateLog')
        return cls._instance

    def post(self, uuid_session, method_name):
        """Registra una entrada en el log con un identificador único (id), el nombre del método y la sesión actual."""
        timestamp = datetime.now().isoformat()
        uuid_cpu = uuid.getnode()  # Genera un identificador único para la CPU como parte de los datos
        log_id = str(uuid.uuid4())  # Genera un identificador único para cada entrada de log como 'id'
        self.table.put_item(
            Item={
                'id': log_id,  # Clave primaria obligatoria
                'uuid_cpu': uuid_cpu,
                'uuid_session': uuid_session,
                'method_name': method_name,
                'timestamp': timestamp
            }
        )

    def list(self, uuid_cpu, uuid_session=None):
        """Lista las entradas del log para una CPU y sesión dadas (si se especifica)."""
        if uuid_session:
            response = self.table.query(
                KeyConditionExpression=Key('uuid_cpu').eq(uuid_cpu) & Key('uuid_session').eq(uuid_session)
            )
        else:
            response = self.table.query(
                KeyConditionExpression=Key('uuid_cpu').eq(uuid_cpu)
            )
        return response.get('Items', [])
