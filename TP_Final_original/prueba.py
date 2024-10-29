import boto3
import json

# Cargar credenciales usando la ruta completa
with open("D:/UADER/3Anio/IS2/Códigos/UADER_IS2_Kazanski_Gabriel/TP_Final/IS2_TPFI_credentials.json") as cred_file:
    creds = json.load(cred_file)

aws_access_key = creds["accesskey"]
aws_secret_key = creds["secretkey"]
region = creds["region"]

# Conexión a DynamoDB
try:
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )
    # Listar tablas para verificar la conexión
    tables = list(dynamodb.tables.all())
    print("Conexión exitosa. Tablas en DynamoDB:", [table.name for table in tables])
except Exception as e:
    print("Error de conexión:", e)
