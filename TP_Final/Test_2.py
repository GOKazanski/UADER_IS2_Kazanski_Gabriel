import unittest
import uuid
import os
import logging
from Components.CorporateData import CorporateData
from Components.CorporateLog import CorporateLog

# Configuración del logger
logger = logging.getLogger('TestLogger')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class TestCorporateComponents(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.corporate_data = CorporateData.getInstance()
        cls.corporate_log = CorporateLog.getInstance()
        cls.session_id = str(uuid.uuid4())
        cls.uuid_cpu = uuid.getnode()
        cls.site_id = "UADER-FCyT-IS2"

    def setUp(self):
        logger.info(f"Iniciando el test: {self._testMethodName}")

    def tearDown(self):
        logger.info(f"Finalizando el test: {self._testMethodName}\n{'-'*60}")

    def test_01_singleton_instance(self):
        corporate_data2 = CorporateData.getInstance()
        corporate_log2 = CorporateLog.getInstance()
        self.assertIs(self.corporate_data, corporate_data2, "CorporateData no es Singleton")
        self.assertIs(self.corporate_log, corporate_log2, "CorporateLog no es Singleton")

    def test_02_getData(self):
        result = self.corporate_data.getData(self.session_id, self.uuid_cpu, self.site_id)
        logger.info(f"Resultado de getData: {result}")
        self.assertIn("sede", result, "No se encontró la clave 'sede' en la respuesta")
        self.assertIn("domicilio", result, "No se encontró la clave 'domicilio' en la respuesta")

    def test_03_getCUIT(self):
        cuit_data = self.corporate_data.getCUIT(self.session_id, self.uuid_cpu, self.site_id)
        logger.info(f"Resultado de getCUIT: {cuit_data}")
        self.assertIn("CUIT", cuit_data, "No se encontró el CUIT en la respuesta")
        self.assertIn("sede", cuit_data, "No se encontró la clave 'sede' en la respuesta")

    def test_04_getSeqID(self):
        seq_id = self.corporate_data.getSeqID(self.session_id, self.uuid_cpu, self.site_id)
        logger.info(f"Resultado de getSeqID: {seq_id}")
        self.assertIn("idSeq", seq_id, "No se encontró 'idSeq' en la respuesta")

    def test_05_post_log(self):
        self.corporate_log.post(self.session_id, "getData")

    def test_06_list_log(self):
        log_entries = self.corporate_log.list(self.uuid_cpu, self.session_id)
        logger.info(f"Entradas en el log para el test: {log_entries}")
        self.assertIsInstance(log_entries, list, "La respuesta de log_entries no es una lista")
        if log_entries:
            self.assertIn("method", log_entries[0], "No se encontró la clave 'method' en la entrada del log")

    def test_07_listCorporateData(self):
        all_data = self.corporate_data.listCorporateData(self.site_id)
        logger.info(f"Datos obtenidos de listCorporateData: {all_data}")
        self.assertIsInstance(all_data, list, "La respuesta de listCorporateData no es una lista")

    def test_08_listCorporateLog(self):
        log_data = self.corporate_data.listCorporateLog(self.uuid_cpu)
        logger.info(f"Datos obtenidos de listCorporateLog: {log_data}")
        self.assertIsInstance(log_data, list, "La respuesta de listCorporateLog no es una lista")

    def test_09_getData_invalid_id(self):
        invalid_id = "INVALID_ID"
        result = self.corporate_data.getData(self.session_id, self.uuid_cpu, invalid_id)
        logger.info(f"Resultado de getData con ID inválido: {result}")
        self.assertIn("error", result, "No se encontró 'error' en la respuesta para ID inválido")

    def test_10_getCUIT_invalid_id(self):
        invalid_id = "INVALID_ID"
        cuit_data = self.corporate_data.getCUIT(self.session_id, self.uuid_cpu, invalid_id)
        logger.info(f"Resultado de getCUIT con ID inválido: {cuit_data}")
        self.assertIn("error", cuit_data, "No se encontró 'error' en la respuesta para ID inválido")

    def test_11_getSeqID_invalid_id(self):
        invalid_id = "INVALID_ID"
        seq_id = self.corporate_data.getSeqID(self.session_id, self.uuid_cpu, invalid_id)
        logger.info(f"Resultado de getSeqID con ID inválido: {seq_id}")
        self.assertIn("error", seq_id, "No se encontró 'error' en la respuesta para ID inválido")

    def test_12_dynamodb_connection_error(self):
        original_table = self.corporate_data.table
        try:
            self.corporate_data.table = self.corporate_data.dynamodb.Table('NonExistentTable')
            result = self.corporate_data.getData(self.session_id, self.uuid_cpu, self.site_id)
            logger.info(f"Resultado de conexión con tabla inexistente: {result}")
            self.assertIn("error", result, "No se encontró 'error' al simular un error de conexión")
        finally:
            self.corporate_data.table = original_table

    def test_13_log_post_entry(self):
        self.corporate_log.post(self.session_id, "testMethod")
        log_entries = self.corporate_log.list(self.uuid_cpu, self.session_id)
        logger.info(f"Entradas de log después de testMethod: {log_entries}")
        self.assertTrue(any(entry.get('method') == 'testMethod' for entry in log_entries),
                        "No se encontró la entrada de log esperada para 'testMethod'")

    def test_14_getData_missing_argument(self):
        result = self.corporate_data.getData(self.session_id, self.uuid_cpu, "")
        logger.info(f"Resultado de getData con argumento vacío: {result}")
        self.assertIn("error", result, "No se encontró 'error' en la respuesta para ID vacío")

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    unittest.main()
