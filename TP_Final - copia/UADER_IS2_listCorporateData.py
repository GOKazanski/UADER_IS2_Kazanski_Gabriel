import json
import botocore
import boto3
import os
from boto3.dynamodb.conditions import Key  # Importación necesaria

class UADER_IS2_listCorporateData:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateData')
        print("Conexión inicializada con la tabla CorporateData")

    def listCorporateData(self, id):
        """Recupera todos los elementos de la tabla CorporateData para el ID proporcionado."""
        print(f"Consultando entradas en CorporateData para el ID: {id}")
        try:
            response = self.table.query(
                KeyConditionExpression=Key('id').eq(id)
            )
            items = response.get('Items', [])
            return items
        except botocore.exceptions.ClientError as e:
            print(f"Error al obtener datos: {e}")
            return json.dumps({"error": str(e)})

def main():
    site_id = "UADER-FCyT-IS2"
    list_corporate_data = UADER_IS2_listCorporateData()
    corporate_data_entries = list_corporate_data.listCorporateData(site_id)
    print("Entradas en la tabla CorporateData:", corporate_data_entries)

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    main()
