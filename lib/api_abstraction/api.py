import request
from .base_api import BaseApi

class Api(BaseApi):
    def __init__(self, name, scheme, authority):
        super.__init__(name, scheme, authority)
    
    def request(self, method, endpoint, params):
        response = request[method](endpoint.get_uri(), params=params)
        return response
