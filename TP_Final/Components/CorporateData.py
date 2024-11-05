import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import botocore
import logging
from decimal import Decimal
from Components.CorporateLog import CorporateLog

# Configuración del logger
logger = logging.getLogger('CorporateDataLogger')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

class CorporateData:
    _instance = None

    @staticmethod
    def getInstance():
        if CorporateData._instance is None:
            CorporateData._instance = CorporateData()
        return CorporateData._instance

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateData')
        logger.debug("Se inicializa la clase CorporateData")

    def getData(self, uuid, uuidCPU, id):
        logger.debug("Se llama a getData, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))
        try:
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if not item:
                return json.dumps({"error": "Registro no encontrado"})
            return json.dumps({
                "sede": item.get('sede'),
                "domicilio": item.get('domicilio'),
                "localidad": item.get('localidad'),
                "provincia": item.get('provincia')
            })
        except botocore.exceptions.ClientError as e:
            logger.error(f'Error al obtener los datos:{str(e)}')
            return json.dumps({"error": str(e)})

    def getCUIT(self, uuid, uuidCPU, id):
        logger.debug("Se llama a getCUIT, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))
        try:
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if item:
                return json.dumps({"sede": item.get('sede'), "CUIT": item.get('CUIT')})
            else:
                logger.error("CUIT no encontrado")
                return json.dumps({"error": "CUIT no encontrado"})
        except botocore.exceptions.ClientError as e:
            logger.error(f'Error al obtener los datos:{str(e)}')
            return json.dumps({"error": str(e)})

    def getSeqID(self, uuid, uuidCPU, id):
        logger.debug("Se llama a getSeqID, uuid: {uuid}, uuidCPU: {uuidCPU}, id: {id}".format(uuid=uuid, uuidCPU=uuidCPU, id=id))
        try:
            response = self.table.get_item(Key={'id': id})
            item = response.get('Item')
            if item and 'idSeq' in item:
                new_idSeq = int(item['idSeq']) + 1
                self.table.update_item(
                    Key={'id': id},
                    UpdateExpression="SET idSeq = :val",
                    ExpressionAttributeValues={':val': Decimal(new_idSeq)},
                    ReturnValues="UPDATED_NEW"
                )
                return json.dumps({"idSeq": new_idSeq})
            else:
                logger.debug("idSeq no encontrado")
                return json.dumps({"error": "idSeq no encontrado"})
        except botocore.exceptions.ClientError as e:
            logger.error(f'Error al obtener los datos:{str(e)}')
            return json.dumps({"error": str(e)})

    @staticmethod
    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

    def listCorporateData(self, id):
        logger.debug("Se llama a listCorporateData, id: {id}".format(id=id))
        try:
            response = self.table.query(KeyConditionExpression=Key('id').eq(id))
            items = response.get('Items', [])
            return items  # Devuelve siempre una lista
        except botocore.exceptions.ClientError as e:
            logger.error(f'Error al obtener los datos: {str(e)}')
            return []

    def listCorporateLog(self, uuid_CPU):
        logger.debug("Se llama a listCorporateLog, uuid_CPU: {uuid_CPU}".format(uuid_CPU=uuid_CPU))
        try:
            self.table = self.dynamodb.Table('CorporateLog')
            response = self.table.scan(FilterExpression=Attr('CPUid').eq(uuid_CPU))
            items = response.get('Items', [])
            return items  # Devuelve siempre una lista
        except botocore.exceptions.ClientError as e:
            logger.error(f'Error al obtener los datos: {str(e)}')
            return []
