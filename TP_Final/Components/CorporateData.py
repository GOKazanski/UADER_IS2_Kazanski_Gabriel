import boto3
from boto3.dynamodb.conditions import Key
import json
import botocore
from decimal import Decimal
from Components.CorporateLog import CorporateLog

class CorporateData:
    # Atributo de clase para almacenar la instancia Singleton
    _instance = None

    @staticmethod
    def getInstance():
        """Obtiene la instancia Singleton de CorporateData. Si no existe, crea una nueva instancia."""
        if CorporateData._instance is None:
            CorporateData._instance = CorporateData()
        return CorporateData._instance

    def __init__(self):
        """Inicializa el recurso de DynamoDB y asigna la tabla CorporateData."""
        self.dynamodb = boto3.resource('dynamodb')  # Conecta con el recurso DynamoDB de AWS
        self.table = self.dynamodb.Table('CorporateData')  # Asigna la tabla 'CorporateData'

    def getData(self, uuid, uuidCPU, id):
        """Recupera información básica de la sede, como domicilio y localidad, usando el ID proporcionado.
        Si el registro no existe, devuelve un mensaje de error en formato JSON."""
        print("Se llama a getData, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))

        try:
            # Realiza la consulta en DynamoDB
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if not item:
                return json.dumps({"error": "Registro no encontrado"})  # Devuelve error si no existe

            # Devuelve datos seleccionados en formato JSON
            return json.dumps({
                "sede": item.get('sede'),
                "domicilio": item.get('domicilio'),
                "localidad": item.get('localidad'),
                "provincia": item.get('provincia')
            })
        except botocore.exceptions.ClientError as e:
            return json.dumps({"error": str(e)})  # Captura errores de cliente y los devuelve en JSON

    def getCUIT(self, uuid, uuidCPU, id):
        """Recupera el CUIT de la sede según el ID proporcionado. Si el registro o el CUIT no se encuentra,
        devuelve un mensaje de error en formato JSON."""
        print("Se llama a getCUIT, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))

        try:
            # Realiza la consulta en DynamoDB
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if item:
                return json.dumps({
                    "sede": item.get('sede'),
                    "CUIT": item.get('CUIT')
                })
            else:
                return json.dumps({"error": "CUIT no encontrado"})
        except botocore.exceptions.ClientError as e:
            return json.dumps({"error": str(e)})

    def getSeqID(self, uuid, uuidCPU, id):
        """Obtiene y actualiza el ID de secuencia (idSeq) de una sede específica. Si el idSeq no existe,
        devuelve un mensaje de error en formato JSON."""
        print("Se llama a getSeqID, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))

        try:
            # Recupera el registro con el ID especificado
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if item and 'idSeq' in item:
                # Incrementa el idSeq en 1 y actualiza la tabla
                new_idSeq = int(item['idSeq']) + 1
                self.table.update_item(
                    Key={'id': id},
                    UpdateExpression="SET idSeq = :val",
                    ExpressionAttributeValues={':val': Decimal(new_idSeq)},
                    ReturnValues="UPDATED_NEW"
                )
                return json.dumps({"idSeq": new_idSeq})  # Devuelve el nuevo idSeq
            else:
                return json.dumps({"error": "idSeq no encontrado"})
        except botocore.exceptions.ClientError as e:
            return json.dumps({"error": str(e)})

    def listCorporateData(self, id):
        """Recupera todos los elementos de la tabla CorporateData y los devuelve como una lista.
        Si ocurre un error durante la operación, captura la excepción y la devuelve en formato JSON."""
        try:
            response = self.table.scan()  # Escanea la tabla para obtener todos los elementos
            return response.get('Items', [])  # Devuelve todos los elementos encontrados
        except botocore.exceptions.ClientError as e:
            return json.dumps({"error": str(e)})

    def listCorporateLog(self, uuid_CPU):
        """Recupera todas las entradas de la tabla CorporateLog, filtrando por uuid_CPU si es necesario.
        Si hay un error en la operación, captura la excepción y la devuelve en formato JSON."""
        try:
            corporate_log_table = self.dynamodb.Table('CorporateLog')  # Asigna la tabla 'CorporateLog'
            response = corporate_log_table.scan()  # Escanea la tabla CorporateLog
            return response.get('Items', [])  # Devuelve todos los elementos encontrados
        except botocore.exceptions.ClientError as e:
            return json.dumps({"error": str(e)})
