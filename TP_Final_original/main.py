import uuid
from corporate_data import CorporateData
from corporate_log import CorporateLog

def main():
    # Generar identificadores únicos para la sesión y CPU
    uuid_session = str(uuid.uuid4())
    uuid_cpu = uuid.getnode()

    # Instanciar las clases Singleton
    corp_data = CorporateData()
    corp_log = CorporateLog()

    # 1. Prueba del método getData (intenta obtener datos de una sede específica)
    sede_id = "existing_id"  # Cambia a un ID válido existente en tu tabla DynamoDB
    data = corp_data.getData(uuid_session, uuid_cpu, sede_id)
    print("Datos de la sede:", data)

    # 2. Prueba del método getCUIT
    cuit_data = corp_data.getCUIT(uuid_session, uuid_cpu, sede_id)
    print("CUIT de la sede:", cuit_data)

    # 3. Prueba del método getSeqID
    seq_id = corp_data.getSeqID(uuid_session, uuid_cpu, sede_id)
    print("Identificador de secuencia único:", seq_id)

    # 4. Prueba del método listCorporateData
    all_data = corp_data.listCorporateData(sede_id)
    print("Listado completo de datos en CorporateData:", all_data)

    # 5. Registrar una actividad de auditoría usando post
    corp_log.post(uuid_session, "getData")
    print("Registro de auditoría añadido en CorporateLog.")

    # 6. Prueba del método list en CorporateLog
    log_entries = corp_log.list(uuid_cpu)
    print("Listado de entradas en CorporateLog para la CPU actual:", log_entries)

if __name__ == "__main__":
    main()
