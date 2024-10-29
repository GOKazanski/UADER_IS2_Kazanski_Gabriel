import boto3
import json
import uuid
from datetime import datetime
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError  # Importar ClientError

# Cargar credenciales desde el archivo JSON
with open("D:/UADER/3Anio/IS2/Códigos/UADER_IS2_Kazanski_Gabriel/TP_Final/IS2_TPFI_credentials.json") as cred_file:
    creds = json.load(cred_file)

aws_access_key = creds["accesskey"]
aws_secret_key = creds["secretkey"]
region = creds["region"]

class CorporateLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
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
        """Registra una entrada en el log con un identificador único."""
        timestamp = datetime.now().isoformat()
        uuid_cpu = uuid.getnode()  # Generar identificador de CPU
        log_id = str(uuid.uuid4())  # Identificador único para cada entrada
        self.table.put_item(
            Item={
                'id': log_id,  # Clave primaria requerida en la tabla
                'uuid_cpu': uuid_cpu,
                'uuid_session': uuid_session,
                'method_name': method_name,
                'timestamp': timestamp
            }
        )

    def list(self, uuid_cpu, uuid_session=None):
        """Lista las entradas del log para una CPU y sesión dadas (si se especifica) usando scan en lugar de query."""
        from boto3.dynamodb.conditions import Attr  # Asegura importar Attr para la condición de filtrado

        try:
            # Usa scan para listar las entradas de CorporateLog
            if uuid_session:
                response = self.table.scan(
                    FilterExpression=Attr('uuid_cpu').eq(uuid_cpu) & Attr('uuid_session').eq(uuid_session)
                )
            else:
                response = self.table.scan(
                    FilterExpression=Attr('uuid_cpu').eq(uuid_cpu)
                )
            return response.get('Items', [])
        except ClientError as e:
            print("Error en la consulta:", e)
            return []
