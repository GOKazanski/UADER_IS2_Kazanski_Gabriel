import boto3
import json
import os

def list_corporate_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateData')
    response = table.scan()
    print(json.dumps(response['Items'], indent=4, default=str))

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    list_corporate_data()
