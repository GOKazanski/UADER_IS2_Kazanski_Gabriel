import boto3

def clear_table(table_name):
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Escanea la tabla y elimina cada elemento
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(Key={'id': each['id']})  # Ajusta si 'id' no es la clave principal

    print(f"Todos los registros de '{table_name}' han sido eliminados.")

if __name__ == "__main__":
    clear_table('CorporateLog')  # Cambia a 'CorporateData' si necesitas limpiar esa tabla
