import requests
from .base_api import BaseApi

class Api(BaseApi):
    def __init__(self, name, scheme, authority, response_transformers):
        super().__init__(name, scheme, authority, response_transformers)
    
    def request(self, endpoint, headers, params):
        response = endpoint.send_request(headers, params)
        return response
