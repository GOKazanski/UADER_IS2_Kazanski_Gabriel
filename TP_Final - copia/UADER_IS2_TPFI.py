import uuid
from datetime import datetime
import json
import os
import logging
from Components.CorporateData import CorporateData, enable_logging as enable_data_logging
from Components.CorporateLog import CorporateLog, enable_logging as enable_log_logging

# Habilitar logging
enable_data_logging()
enable_log_logging()
logger = logging.getLogger('MainLogger')

def main():
    # Generación automática de identificadores y timestamp
    session_id = str(uuid.uuid4())
    uuid_cpu = uuid.getnode()
    site_id = "UADER-FCyT-IS2"

    # Instancias Singleton de CorporateData y CorporateLog
    logger.info("Instanciando objetos de CorporateData y CorporateLog")
    corporate_data = CorporateData.getInstance()
    corporate_log = CorporateLog.getInstance()

    # Llamada a getData
    logger.info("Obteniendo datos de la sede")
    data = corporate_data.getData(session_id, uuid_cpu, site_id)
    try:
        formatted_data = json.loads(data)
        logger.info(f"Datos obtenidos:\n{json.dumps(formatted_data, indent=2, ensure_ascii=False)}")
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar el JSON en getData: {str(e)}")

    # Registrar operación en CorporateLog - método post
    logger.info("Registrando operación en log para getData")
    corporate_log.post(session_id, "getData")

    # Llamada a getCUIT
    logger.info("Obteniendo CUIT de la sede")
    cuit_data = corporate_data.getCUIT(session_id, uuid_cpu, site_id)
    try:
        formatted_data = json.loads(cuit_data)
        logger.info(f"CUIT obtenido:\n{json.dumps(formatted_data, indent=2, ensure_ascii=False)}")
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar el JSON en getCUIT: {str(e)}")

    # Registrar operación en CorporateLog - método post
    logger.info("Registrando operación en log para getCUIT")
    corporate_log.post(session_id, "getCUIT")

    # Llamada a getSeqID
    logger.info("Obteniendo ID de secuencia")
    seq_id = corporate_data.getSeqID(session_id, uuid_cpu, site_id)
    try:
        formatted_data = json.loads(seq_id)
        logger.info(f"ID de secuencia obtenido:\n{json.dumps(formatted_data, indent=2, ensure_ascii=False)}")
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar el JSON en getSeqID: {str(e)}")

    # Registrar operación en CorporateLog - método post
    logger.info("Registrando operación en log para getSeqID")
    corporate_log.post(session_id, "getSeqID")

    # Listar registros en CorporateData
    logger.info("Listando registros en CorporateData")
    log_entries_corporate_data = corporate_data.listCorporateData(site_id)
    logger.info(f"Entradas de CorporateData:\n{log_entries_corporate_data}")

    # Listar registros en CorporateLog
    logger.info("Listando registros en CorporateLog")
    log_entries_corporate_log = corporate_data.listCorporateLog(uuid_cpu)
    logger.info(f"Entradas de CorporateLog:\n{log_entries_corporate_log}")

    # Consultar el log usando CorporateLog - método list
    logger.info("Consultando registros en CorporateLog")
    log_entries_list = corporate_log.list(uuid_cpu, session_id)
    logger.info(f"Entradas de log consultadas:\n{log_entries_list}")

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
    main()
