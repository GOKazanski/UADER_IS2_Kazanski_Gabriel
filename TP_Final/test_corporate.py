import unittest
from IS2_TPFI_credentials import aws_access_key, aws_secret_key, region
from corporate_data import CorporateData
from corporate_log import CorporateLog
import uuid

class TestCorporateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.corp_data = CorporateData(aws_access_key, aws_secret_key, region)
        cls.corp_log = CorporateLog(aws_access_key, aws_secret_key, region)
        cls.uuid_session = str(uuid.uuid4())
        cls.uuid_cpu = uuid.getnode()

    def test_singleton_instance(self):
        corp_data2 = CorporateData(aws_access_key, aws_secret_key, region)
        self.assertIs(self.corp_data, corp_data2)

    def test_getData(self):
        result = self.corp_data.getData(self.uuid_session, self.uuid_cpu, "some_id")
        self.assertIn("id", result)  # Assuming id exists in response structure

    def test_post_log(self):
        self.corp_log.post(self.uuid_session, "getData")
        logs = self.corp_log.list(self.uuid_cpu)
        self.assertGreater(len(logs), 0)

if __name__ == "__main__":
    unittest.main()
