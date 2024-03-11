import copy
from enum import IntEnum
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict, computed_field

from . import config


class IPVersion(IntEnum):
    IPV4_SHARED = 3
    IPV4 = 4
    IPV6 = 6


class Proxy6Balance(BaseModel):
    date_mod: datetime
    status: str
    user_id: str
    balance: float
    currency: str


class Proxy6Price(Proxy6Balance):
    price: float
    period: int
    count: int
    price_single: float


class Proxy6Purchase(Proxy6Balance):
    price: float
    period: int
    count: int
    status: str
    country: str
    proxies: list['Proxy6Proxy']

    @model_validator(mode='before')
    @classmethod
    def add_country_to_proxies(cls, response: dict) -> dict:
        response = copy.deepcopy(response)
        for proxy_dict in response['list'].values():
            proxy_dict['country'] = response['country']
        response['proxies'] = response.pop('list').values()

        return response


class Proxy6Proxy(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    id: str
    ip: str
    host: str
    port: str
    user: str
    password: str = Field(..., validation_alias='pass')
    protocol: str = Field(..., validation_alias='type')
    country: str
    date: datetime
    date_end: datetime
    descr: str | None = None
    active: str

    def __str__(self):
        return self.url

    @field_validator('active', mode='after')
    @classmethod
    def is_active(cls, value: Literal['1', '0'] | bool) -> bool:
        return bool(int(value))

    @property
    def url(self) -> str:
        return "{}://{}:{}@{}:{}".format(self.protocol, self.user, self.password, self.host, self.port)

    @property
    def is_expired(self) -> bool:
        return self.date_end <= datetime.now()
