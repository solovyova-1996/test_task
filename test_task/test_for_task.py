from unittest import TestCase
from task import data_sha_256


class TestClass(TestCase):
    def setUp(self) -> None:
        self.test_str = 'helloloo'
        self.expected_str_hash = '78c3e782b67965895e2e0120ae4d739e266028c113ec6b3566d522f6ea328c93'

    def tearDown(self) -> None:
        del self.test_str
        del self.expected_str_hash

    def test_data_sha_256(self):
        res = data_sha_256(self.test_str)
        return self.assertEqual(res, self.expected_str_hash)
