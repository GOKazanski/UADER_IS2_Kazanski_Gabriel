import boto3
import botocore
import json
import os

from Components.CorporateLog import CorporateLog
from boto3.dynamodb.conditions import Attr

class UADER_IS2_listLog:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateLog')
        print("Inicializada la conexión con la tabla CorporateLog")

    def listCorporateLog(self):
        """Obtiene todas las entradas de la tabla CorporateLog."""
        try:
            response = self.table.scan()
            items = response.get('Items', [])
            print(f"Se encontraron {len(items)} entradas en CorporateLog.")
            for item in items:
                print(f"Entrada:\n{json.dumps(item, indent=2, default=self.decimal_default, ensure_ascii=False)}\n")
            return items
        except botocore.exceptions.ClientError as e:
            print(f"Error al obtener datos: {e}")
            return json.dumps({"error": str(e)})

    @staticmethod
    def decimal_default(obj):
        """Convierte objetos Decimal a float para que sean serializables en JSON."""
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError

def main():
    log_listLog = UADER_IS2_listLog()
    log_entries = log_listLog.listCorporateLog()
    print("Entradas en la tabla CorporateLog:", log_entries)

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    main()
