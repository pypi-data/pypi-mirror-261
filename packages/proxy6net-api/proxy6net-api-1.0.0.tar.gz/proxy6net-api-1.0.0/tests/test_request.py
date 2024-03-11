import unittest
from requests import Session
from unittest.mock import patch, Mock
from src.proxy6net_api.api import Proxy6Request
from src.proxy6net_api.errors import Proxy6Exception


class TestRequest(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Session()
        self.request = Proxy6Request(auth_token='auth_token', session=self.session)

    def test_request(self):
        response_mock = Mock(json=Mock(return_value={'status': 'yes'}))
        with patch.object(self.session, 'get', return_value=response_mock) as mock_get:
            self.request._request(method='meth', options={'a': 1}, b=2)
            
            self.assertDictEqual(mock_get.call_args.kwargs, dict(params={'b': 2}, a=1))

    def test_request_bad_status_raises(self):
        response = {
            "status": "no",
            "error_id": 100,
            "error": "Error key"
        }
        response_mock = Mock(json=Mock(return_value=response))

        with patch.object(self.session, 'get', return_value=response_mock):
            self.assertRaises(Proxy6Exception, self.request._request, method='meth')
