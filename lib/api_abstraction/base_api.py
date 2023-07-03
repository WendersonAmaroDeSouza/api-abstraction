import request

class BaseApi:
    def __init__(self, name, scheme, authority):
        self.name = name
        self.scheme = scheme
        self.authority = authority
        self._resources = []
    
    def add_resource(self, resource):
        self._resources.append(resource)

class Resource:
    def __init__(self, name):
        self.name = name
        self._endpoints = []
    
    def add_endpoint(self, endpoint):
        self._endpoints.append(endpoint)

class Endpoint:
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource
    
    def get_uri(self):
        api = self.resource.api
        scheme = api.scheme
        authority = api.authority
        return f'{scheme}{authority}{path}'
