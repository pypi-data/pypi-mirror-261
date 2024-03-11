import unittest
from datetime import datetime
from unittest.mock import patch
from src.proxy6net_api import Proxy6API
from src.proxy6net_api import types
from .payload import fake_proxy


class TestProxy6Request(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Proxy6API(auth_token='token')

    def test_get_balance(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "date_mod": "2023-10-01 20:20:57",
        }
        with patch.object(self.api, '_request', return_value=response):
            self.assertEqual(self.api.get_balance(), types.Proxy6Balance(**response))

    def test_available_count(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "count": 971,
            "date_mod": "2023-10-01 20:20:57",
        }
        with patch.object(self.api, '_request', return_value=response):
            self.assertEqual(self.api.get_available_count(country_code='ru', ipv='IPV4'), 971)

    def test_available_countries(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "list": ["ru", "ua", "us"],
            "date_mod": "2023-10-01 20:20:57",
        }
        with patch.object(self.api, '_request', return_value=response):
            self.assertEqual(self.api.get_available_countries(ipv='IPV4'), response['list'])

    def test_get_proxy(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "list_count": 4,
            "date_mod": "2023-10-01 20:20:57",
            "list": {
                "11": {
                    "id": "11",
                    "ip": "2a00:1838:32:19f:45fb:2640::330",
                    "host": "185.22.134.250",
                    "port": "7330",
                    "user": "5svBNZ",
                    "pass": "iagn2d",
                    "type": "http",
                    "country": "ru",
                    "date": "2016-06-19 16:32:39",
                    "date_end": "2016-07-12 11:50:41",
                    "unixtime": 1466379159,
                    "unixtime_end": 1468349441,
                    "descr": "",
                    "active": "1"
                },
                "14": {
                    "id": "14",
                    "ip": "2a00:1838:32:198:56ec:2696::386",
                    "host": "185.22.134.242",
                    "port": "7386",
                    "user": "nV5TFK",
                    "pass": "3Itr1t",
                    "type": "http",
                    "country": "ru",
                    "date": "2016-06-27 16:06:22",
                    "date_end": "2016-07-11 16:06:22",
                    "unixtime": 1466379159,
                    "unixtime_end": 1468349441,
                    "descr": "",
                    "active": "1"
                }
            }
        }
        proxies = [types.Proxy6Proxy(**proxy_data) for proxy_data in response['list'].values()]

        with patch.object(self.api, '_request', return_value=response):
            self.assertListEqual(self.api.get_proxies(), proxies)

    def test_set_protocol(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "date_mod": "2023-10-01 20:20:57",
        }
        proxy = fake_proxy(id='1', type='http')

        with patch.object(self.api, '_request', return_value=response):
            self.api.set_protocol(proxy, protocol='socks')
            self.assertEqual(proxy.protocol, 'socks')

    def test_set_descr(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "count": 4,
            "date_mod": "2023-10-01 20:20:57",
        }
        proxy = fake_proxy(id='1')

        with patch.object(self.api, '_request', return_value=response):
            self.api.set_descr(proxy, descr='new_description')
            self.assertEqual(proxy.descr, 'new_description')

    def test_buy(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": 42.5,
            "currency": "RUB",
            "count": 1,
            "price": 6.3,
            "period": 7,
            "country": "ru",
            "date_mod": "2023-10-01 20:20:57",
            "list": {
                "15": {
                    "id": "15",
                    "ip": "2a00:1838:32:19f:45fb:2640::330",
                    "host": "185.22.134.250",
                    "port": "7330",
                    "user": "5svBNZ",
                    "pass": "iagn2d",
                    "type": "http",
                    "date": "2016-06-19 16:32:39",
                    "date_end": "2016-07-12 11:50:41",
                    "unixtime": 1466379159,
                    "unixtime_end": 1468349441,
                    "active": "1"
                }
            }
        }

        with patch.object(self.api, '_request', return_value=response):
            purchase = self.api.buy_proxies(count=1, days=1, country_code='ru', ipv='IPV4')
            proxy = purchase.proxies[0]
            self.assertEqual(proxy.id, '15')

    def test_prolong(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": 29,
            "currency": "RUB",
            "price": 12.6,
            "period": 7,
            "count": 1,
            "list": {
                "15": {
                    "id": 15,
                    "date_end": "2016-07-15 06:30:27",
                    "unixtime_end": 1466379159
                },
                "16": {
                    "id": 15,
                    "date_end": "2018-07-15 06:30:27",
                    "unixtime_end": 1466379159
                }
            }
        }
        proxy15 = fake_proxy('15')
        proxy16 = fake_proxy('16')

        with patch.object(self.api, '_request', return_value=response):
            self.api.prolong_proxies(proxy15, proxy16, days=1)
            self.assertEqual(proxy15.date_end, datetime.fromisoformat(response['list']['15']['date_end']))
            self.assertEqual(proxy16.date_end, datetime.fromisoformat(response['list']['16']['date_end']))

    def test_delete(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "count": 4
        }
        with patch.object(self.api, '_request', return_value=response):
            self.assertIsNone(self.api.delete_proxies(fake_proxy(id='1')))

    def test_check(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB",
            "proxy_id": 15,
            "proxy_status": True
        }
        with patch.object(self.api, '_request', return_value=response):
            status = self.api.check_proxy(fake_proxy(id='15'))
            self.assertEqual(status, response['proxy_status'])

    def test_ip_auth(self):
        response = {
            "status": "yes",
            "user_id": "1",
            "balance": "48.80",
            "currency": "RUB"
        }
        with patch.object(self.api, '_request', return_value=response):
            self.assertIsNone(self.api.ip_auth())
