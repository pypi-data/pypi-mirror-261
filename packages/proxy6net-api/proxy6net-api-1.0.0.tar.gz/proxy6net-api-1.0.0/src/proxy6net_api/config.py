

API_URL = 'https://proxy6.net/api/{api_token}/{method}'

ERROR_CODES = {
    30:  'Unknown error',
    100: 'Authorization error, wrong key',
    105: 'The API was accessed from an incorrect IP (if the restriction is enabled), or an incorrect IP address format',
    110: 'Wrong method',
    200: 'Wrong proxies quantity, wrong amount or no quantity input',
    210: 'Period error, wrong period input (days) or no input',
    220: 'Country error, wrong country input (iso2 for country input) or no input',
    230: 'Error of the list of the proxy numbers. Proxy numbers have to divided with comas',
    240: 'The proxy version is specified incorrectly',
    250: 'Tech description error (maximum length is 50)',
    260: 'Proxy type (protocol) error. Incorrect or missing',
    300: 'Proxy amount error. Appears after attempt of purchase of more proxies than available on the service',
    400: 'Balance error. Zero or low balance on your account',
    404: 'Element error. The requested item was not found',
    410: 'Error calculating the cost. The total cost is less than or equal to zero',
}

ERROR_UNKNOWN = 'Unknown Error'
