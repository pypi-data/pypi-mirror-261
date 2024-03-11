from .types import Proxy6Proxy


def ids_from_proxies(*proxies: Proxy6Proxy) -> str:
    return ','.join(p.id for p in proxies)
