# Proxy6 API wrapper
Unofficial API wrapper for [proxy6.net](https://proxy6.net/) using pydantic


## Installation
```commandline
pip install proxy6net-api
```
## Basic usage
Get your API token [here](https://proxy6.net/user/developers)
### Create API wrapper instance

```python
from proxy6net_api import Proxy6API

api = Proxy6API(auth_token='your_token')
```

### Get balance
```python
balance = api.get_balance()
f'{balance.balance=}, {balance.currency=}'

# balance.balance = 518.20, balance.currency='RUB'
```
### Buy proxies
```python
purchase = api.buy_proxies(count=3, days=5, country_code='ru', ipv='IPV6', protocol='http')
len(purchase.proxies)

# 3
```
### Use proxy
```python
import requests

proxy = api.get_proxies(state='active')[0]
response = requests.get('https://api64.ipify.org?format=json', proxies={'http': str(proxy), 'https': proxy.url})

assert response.json()['ip'] == proxy.ip
```
## Other methods
```python
help(Proxy6API)
```
## Error handling
```python
from proxy6net_api import Proxy6Exception

try:
    proxies = Proxy6API(auth_token='invalid token').get_proxies()
except Proxy6Exception as err:
    print(f'Error description: {err.description}. Error code: {err.code}')
    
    # Error description: Authorization error, wrong key. Error code: 100
```
