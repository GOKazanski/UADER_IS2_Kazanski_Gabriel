import uuid
import os
from Components.CorporateData import CorporateData
from Components.CorporateLog import CorporateLog
from datetime import datetime

def main():
    # Generación automática de identificadores y timestamp
    session_id = str(uuid.uuid4())  # Genera un identificador único para la sesión actual
    uuid_cpu = uuid.getnode()       # Obtiene un identificador único para la CPU del equipo
    site_id = "UADER-FCyT-IS2"      # ID de la sede a consultar en la base de datos

    # Timestamp actual en formato legible
    timestamp = datetime.now().isoformat()  # Genera el timestamp actual en formato ISO 8601

    # Instancias Singleton de CorporateData y CorporateLog
    print("Instanciando objetos:")
    corporate_data = CorporateData.getInstance()  # Obtiene la instancia Singleton de CorporateData
    corporate_log = CorporateLog.getInstance()    # Obtiene la instancia Singleton de CorporateLog

    # Llamada a getData
    print("Obteniendo datos:")
    data = corporate_data.getData(session_id, uuid_cpu, site_id)  # Obtiene datos de la sede
    print("Datos obtenidos:", data)

    # Registrar operación con CorporateLog - método post
    print("\nRegistrando operación en log:")
    corporate_log.post(session_id, "getData")  # Registra en el log que se llamó a getData

    # Llamada a getCUIT
    print("\nObteniendo CUIT:")
    cuit_data = corporate_data.getCUIT(session_id, uuid_cpu, site_id)  # Obtiene el CUIT de la sede
    print("CUIT:", cuit_data)

    # Registrar operación con CorporateLog - método post
    print("\nRegistrando operación en log:")
    corporate_log.post(session_id, "getCUIT")  # Registra en el log que se llamó a getCUIT

    # Llamada a getSeqID
    print("\nObteniendo ID de secuencia:")
    seq_id = corporate_data.getSeqID(session_id, uuid_cpu, site_id)  # Obtiene el siguiente ID de secuencia
    print("ID de secuencia:", seq_id)

    # Registrar operación con CorporateLog - método post
    print("\nRegistrando operación en log:")
    corporate_log.post(session_id, "getSeqID")  # Registra en el log que se llamó a getSeqID

    # Ejemplo de cómo listar registros con CorporateData y CorporateLog (descomentar si es necesario)
    # print("\nListando registros CorporateData:")
    # log_entries = corporate_data.listCorporateData(site_id)  # Lista todos los registros de CorporateData
    # print("Entradas de log:", log_entries)

    # print("\nListando registros CorporateLog:")
    # log_entries = corporate_data.listCorporateLog(uuid_cpu)  # Lista todos los registros de CorporateLog para la CPU
    # print("Entradas de log:", log_entries)

    # Consultar el log usando CorporateLog - método list
    print("\nConsultando registros en log:")
    log_entries = corporate_log.list(uuid_cpu, session_id)  # Consulta el log filtrando por CPU y sesión
    print("Entradas de log:", log_entries)

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
    main()
