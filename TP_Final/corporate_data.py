import boto3
import uuid
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class CorporateData:
    _instance = None

    def __new__(cls, aws_access_key, aws_secret_key, region):
        if cls._instance is None:
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
        try:
            response = self.table.get_item(Key={'id': id})
            return response.get('Item', {"error": "Record not found"})
        except (NoCredentialsError, PartialCredentialsError) as e:
            return {"error": str(e)}

    def getCUIT(self, uuid_session, uuid_cpu, id):
        data = self.getData(uuid_session, uuid_cpu, id)
        return {"CUIT": data.get('CUIT', 'CUIT not found')}

    def getSeqID(self, uuid_session, uuid_cpu, id):
        data = self.getData(uuid_session, uuid_cpu, id)
        seq_id = data.get('idSeq', 0) + 1
        self.table.update_item(
            Key={'id': id},
            UpdateExpression="set idSeq = :seq",
            ExpressionAttributeValues={':seq': seq_id}
        )
        return {"idSeq": seq_id}

    def listCorporateData(self, id):
        response = self.table.scan()
        return response.get('Items', [])
