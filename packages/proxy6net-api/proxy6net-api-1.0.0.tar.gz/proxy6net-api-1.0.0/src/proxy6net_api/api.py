import requests
from functools import cached_property
from typing import Literal, Any
from . import config
from . import types
from .utils import ids_from_proxies
from .errors import Proxy6Exception


class Proxy6Request:
    """ Base class that performs requests. """

    def __init__(self, auth_token=None, session=None):
        self.auth_token = auth_token
        self._session = session

    def __repr__(self):
        return '<{}(auth_token={}, session={})>'.format(self.__class__.__name__, self.auth_token, self._session)

    @cached_property
    def session(self):
        return self._session if self._session else requests.Session()

    def _request(self, method: str, options: dict[str, Any] | None = None, **params: Any) -> dict:
        url = config.API_URL.format(api_token=self.auth_token, method=method)
        response = self.session.get(url, params=params, **(options or {}))
        response.raise_for_status()

        data = response.json()
        if data.get('status') != 'yes':
            raise Proxy6Exception(code=data.get('error_id', None))

        return data


class Proxy6API(Proxy6Request):
    """ proxy6.net API wrapper """

    def get_balance(self, **options: Any) -> types.Proxy6Balance:
        response = self._request(method='', options=options)
        return types.Proxy6Balance(**response)

    def get_price(self, *, count: int, days: int, ipv: Literal['IPV4_SHARED', 'IPV4', 'IPV6'], **options: Any) -> types.Proxy6Price:
        """ Calculate order cost
        :param count: number of proxies
        :param days: number of days
        :param ipv: Proxy IP version
        :param options: Additional options to pass in request
        """
        response = self._request(method='getprice', count=count, period=days, version=types.IPVersion[ipv], options=options)
        return types.Proxy6Price(**response)

    def get_available_count(self, *, country_code: str, ipv: Literal['IPV4_SHARED', 'IPV4', 'IPV6'], **options: Any) -> int:
        """ Available number of proxies for a specific country
        :param country_code: Country code in iso2 format (length=2)
        :param ipv: Proxy IP version
        :param options: Additional options for passing in request
        """
        response = self._request(method='getcount', country=country_code, version=types.IPVersion[ipv], options=options)
        return response['count']

    def get_available_countries(self, *, ipv: Literal['IPV4_SHARED', 'IPV4', 'IPV6'], **options: Any) -> list[str]:
        """ List of available country codes
        :param ipv: Proxy IP version
        :param options: Additional options for passing in request
        """
        response = self._request(method='getcountry', version=types.IPVersion[ipv], options=options)
        return response['list']

    def get_proxies(self,
                    *,
                    state: Literal['all', 'active', 'expired', 'expiring'] = 'all',
                    descr: str | None = None,
                    page: int = 1,
                    limit: int = 1000,
                    **options: Any
                    ) -> list[types.Proxy6Proxy]:
        """ List of your proxies
        :param state: State returned proxies
        :param descr: Technical comment you have entered when purchasing proxy.
         If you filled in this parameter, then the reply would display only those proxies with given parameter
        :param page: Page number to output
        :param limit: Number of proxies to output on page
        :param options: Additional options for passing in request
        """
        response = self._request(method='getproxy', state=state, descr=descr, page=page, limit=limit, options=options)

        proxies = [types.Proxy6Proxy(**proxy) for proxy in (response['list'] or {}).values()]     # empty `list` is list type else dict
        return proxies

    def set_protocol(self, *proxies: types.Proxy6Proxy, protocol: Literal['http', 'socks'], **options: Any) -> None:
        """ Change proxy protocol
        :param proxies: List of internal proxies ids
        :param protocol: Sets the type (protocol): 'http' - HTTPS or 'socks' - SOCKS5.
        :param options: Additional options for passing in request
        """
        response = self._request(method='settype', ids=ids_from_proxies(*proxies), type=protocol, options=options)
        for proxy in proxies:
            proxy.protocol = protocol

    def set_descr(self, *proxies: types.Proxy6Proxy, descr: str, **options: Any) -> None:
        """ Set technical comment
        :param descr: New technical comment with a maximum length of 50 characters
        :param proxies: List of internal proxies ids
        :param options: Additional options for passing in request
        """
        response = self._request(method='setdescr', ids=ids_from_proxies(*proxies), new=descr, options=options)
        for proxy in proxies:
            proxy.descr = descr

    def buy_proxies(self,
                    *,
                    count: int,
                    days: int,
                    country_code: str,
                    ipv: Literal['IPV4_SHARED', 'IPV4', 'IPV6'],
                    protocol: Literal['http', 'socks'] = 'http',
                    descr: str | None = None,
                    auto_prolong: bool | None = None,
                    **options: Any
                    ) -> types.Proxy6Purchase:
        """ Proxy purchase
        :param count: Amount of proxies for purchase
        :param days: Period for which proxies are purchased in days
        :param country_code: Country in iso2 format
        :param ipv: IP version
        :param protocol: Proxies type (protocol): 'socks' or 'http' (default)
        :param descr: Technical comment for proxies list with a maximum length of 50 characters
        :param auto_prolong: if not None enables the purchased proxy auto-renewal
        :param options: Additional options for passing in request
        """
        response = self._request(
            method='buy',
            count=count,
            period=days,
            country=country_code,
            version=ipv,
            type=protocol,
            descr=descr,
            auto_prolong=auto_prolong,
            options=options
        )
        return types.Proxy6Purchase(**response)

    def prolong_proxies(self, *proxies: types.Proxy6Proxy, days: int, **options: Any) -> None:
        """ Proxies prolongation
        :param days: Prolongation period in days
        :param proxies: List of internal proxies
        :param options: Additional options for passing in request
        """
        response = self._request(method='prolong', ids=ids_from_proxies(*proxies), period=days, options=options)
        for proxy in proxies:
            proxy.date_end = response['list'][proxy.id]['date_end']

    def delete_proxies(self, *proxies: types.Proxy6Proxy, **options: Any) -> None:
        """ Delete proxies
        :param proxies: List of internal proxies
        :param options: Additional options for passing in request
        """
        self._request(method='delete', ids=ids_from_proxies(*proxies), options=options)

    def check_proxy(self, proxy: types.Proxy6Proxy, **options: Any) -> bool:
        """ Proxy validity check
        :param proxy: single proxy
        :param options: Additional options for passing in request
        """
        response = self._request(method='check', ids=proxy.id, options=options)
        return response['proxy_status']

    def ip_auth(self, *ip: str, **options: Any) -> None:
        """ Bind or delete proxy authorization by ip
        :param ip: A list of ip-addresses to bind or "delete" - to remove the binding
        :param options: Additional options for passing in request
        """
        self._request(method='ipauth', ip=','.join(ip), options=options)
