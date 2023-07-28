import requests
from .base_api import BaseApi

class Api(BaseApi):
    def __init__(self, name, scheme, authority):
        super().__init__(name, scheme, authority)
    
    def request(self, endpoint, headers, params):
        response = endpoint.send_request(headers, params)
        return response
