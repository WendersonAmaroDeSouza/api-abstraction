from enum import Enum
import requests

class BaseApi:
    def __init__(self, name, scheme, authority):
        self.name = name
        self.scheme = scheme
        self.authority = authority
        self._resources = []
    
    def add_resource(self, resource):
        self._resources.append(resource)
        resource.api = self

class Resource:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        api.add_resource(self)
        self._endpoints = []
    
    def add_endpoint(self, endpoint):
        self._endpoints.append(endpoint)
        endpoint.resource = self

class Endpoint:
    def __init__(self, path, http_method, resource):
        self.path = path
        self.http_method = http_method
        self.resource = resource
        resource.add_endpoint(self)
    
    def get_uri(self):
        api = self.resource.api
        scheme = api.scheme
        authority = api.authority
        return f'{scheme}{authority}{self.path}'
    
    def send_request(self, headers, params):
        response = getattr(requests, self.http_method.value)(self.get_uri())
        print(f'{response.status_code}: [{self.http_method.value}] {self.get_uri()}')
        return response

class HTTPMethod(Enum):
    POST = 'post'
    GET = 'get'
    UPDATE = 'update'
    PATCH = 'patch'
    DELETE = 'delete'
    OPTIONS = 'options'
