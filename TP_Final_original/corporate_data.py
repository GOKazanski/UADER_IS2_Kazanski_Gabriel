import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Cargar credenciales desde la ruta completa del archivo JSON
with open("D:/UADER/3Anio/IS2/Códigos/UADER_IS2_Kazanski_Gabriel/TP_Final/IS2_TPFI_credentials.json") as cred_file:
    creds = json.load(cred_file)

aws_access_key = creds["accesskey"]
aws_secret_key = creds["secretkey"]
region = creds["region"]

class CorporateData:
    _instance = None  # Atributo de clase para almacenar la instancia Singleton

    def __new__(cls):
        if cls._instance is None:
            # Crear una nueva instancia si no existe y configurarla para usar DynamoDB
            cls._instance = super(CorporateData, cls).__new__(cls)
            cls._instance.dynamodb = boto3.resource(
                'dynamodb',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=region
            )
            cls._instance.table = cls._instance.dynamodb.Table('CorporateData')
        return cls._instance

    def getData(self, uuid_session, uuid_cpu, id):
        """Recupera datos de la sede dada por el ID. Retorna JSON con los datos o mensaje de error."""
        try:
            response = self.table.get_item(Key={'id': id})
            return response.get('Item', {"error": "Record not found"})
        except (NoCredentialsError, PartialCredentialsError) as e:
            return {"error": str(e)}

    def getCUIT(self, uuid_session, uuid_cpu, id):
        """Obtiene el CUIT de la sede especificada por el ID."""
        data = self.getData(uuid_session, uuid_cpu, id)
        return {"CUIT": data.get('CUIT', 'CUIT not found')}

    def getSeqID(self, uuid_session, uuid_cpu, id):
        """Obtiene y aumenta en 1 el identificador de secuencia único en la base de datos."""
        data = self.getData(uuid_session, uuid_cpu, id)
        seq_id = data.get('idSeq', 0) + 1
        self.table.update_item(
            Key={'id': id},
            UpdateExpression="set idSeq = :seq",
            ExpressionAttributeValues={':seq': seq_id}
        )
        return {"idSeq": seq_id}

    def listCorporateData(self, id):
        """Lista todos los registros de la tabla CorporateData."""
        response = self.table.scan()
        return response.get('Items', [])
