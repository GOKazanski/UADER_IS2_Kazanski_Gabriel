import boto3
from datetime import datetime

class CorporateLog:
    _instance = None

    def __new__(cls, aws_access_key, aws_secret_key, region):
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
        timestamp = datetime.now().isoformat()
        self.table.put_item(
            Item={
                'uuid_session': uuid_session,
                'method_name': method_name,
                'timestamp': timestamp
            }
        )

    def list(self, uuid_cpu, uuid_session=None):
        if uuid_session:
            response = self.table.query(
                KeyConditionExpression=Key('uuid_cpu').eq(uuid_cpu) & Key('uuid_session').eq(uuid_session)
            )
        else:
            response = self.table.query(
                KeyConditionExpression=Key('uuid_cpu').eq(uuid_cpu)
            )
        return response.get('Items', [])
