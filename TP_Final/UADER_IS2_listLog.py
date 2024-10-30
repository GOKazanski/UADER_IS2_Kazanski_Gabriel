import boto3
import json
import uuid
import os

def list_corporate_log():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateLog')
    uuid_cpu = uuid.getnode()
    response = table.scan(
        FilterExpression="CPUid = :cpu_id",
        ExpressionAttributeValues={':cpu_id': uuid_cpu}
    )
    print(json.dumps(response['Items'], indent=4, default=str))

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    list_corporate_log()
