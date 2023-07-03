import request
from .base_api import BaseApi

class Api(BaseApi):
    def __init__(self, name, scheme, authority):
        super.__init__(name, scheme, authority)
