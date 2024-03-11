import unittest
from src.proxy6net_api.errors import Proxy6Exception
from src.proxy6net_api.config import ERROR_CODES, ERROR_UNKNOWN
from src.proxy6net_api.api import Proxy6API
from src.proxy6net_api import types


def raise_api_error(code):
    raise Proxy6Exception(code=code)


class TestErrors(unittest.TestCase):

    def setUp(self) -> None:
        self.api = Proxy6API(auth_token='token')

    def test_error_known_code(self):
        for code in ERROR_CODES:
            with self.subTest(code=code):
                self.assertRaisesRegex(Proxy6Exception, f'[{ERROR_CODES.get(code)}]', raise_api_error, code=code)

    def test_error_unknown_code(self):
        self.assertRaisesRegex(Proxy6Exception, ERROR_UNKNOWN, raise_api_error, code=1e10)
