import unittest
from corporate_data import CorporateData
from corporate_log import CorporateLog
import uuid

class TestCorporateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crear instancias Singleton de las clases CorporateData y CorporateLog para las pruebas
        cls.corp_data = CorporateData()
        cls.corp_log = CorporateLog()
        cls.uuid_session = str(uuid.uuid4())  # Generar un UUID único para la sesión
        cls.uuid_cpu = uuid.getnode()  # Obtener un identificador de CPU único

    def test_singleton_instance(self):
        """Verifica que CorporateData y CorporateLog son instancias Singleton."""
        corp_data2 = CorporateData()
        corp_log2 = CorporateLog()
        self.assertIs(self.corp_data, corp_data2)
        self.assertIs(self.corp_log, corp_log2)

    def test_getData(self):
        """Prueba el método getData de CorporateData."""
        result = self.corp_data.getData(self.uuid_session, self.uuid_cpu, "non_existing_id")
        self.assertIn("error", result)  # Verifica el mensaje de error cuando el registro no se encuentra

    def test_post_log(self):
        """Prueba el método post de CorporateLog y valida que se haya registrado la entrada."""
        self.corp_log.post(self.uuid_session, "getData")
        logs = self.corp_log.list(self.uuid_cpu)
        self.assertGreater(len(logs), 0)

if __name__ == "__main__":
    unittest.main()
