__author__ = "Nikita Bulavinov"
__version__ = '1.0.0'

from .api import Proxy6API
from .errors import Proxy6Exception
from . import config as proxy6config

__all__ = ('Proxy6API', 'proxy6config', 'Proxy6Exception')
