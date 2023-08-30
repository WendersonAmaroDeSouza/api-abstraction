from enum import Enum
from types import SimpleNamespace
import requests

class BaseApi:
    def __init__(self, name, scheme, authority, transformers):
        self.name = name
        self.scheme = scheme
        self.authority = authority
        self.transformers = transformers
        self._resources = []
        self.resources = SimpleNamespace()
    
    def add_resource(self, resource):
        self._resources.append(resource)
        setattr(self.resources, resource.name, resource)
        resource.api = self

class Resource:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        api.add_resource(self)
        self._endpoints = []
        self.endpoints = SimpleNamespace()
    
    def add_endpoint(self, endpoint):
        self._endpoints.append(endpoint)
        setattr(self.endpoints, endpoint.name, endpoint)
        endpoint.resource = self

class Endpoint:
    def __init__(
            self, 
            path, 
            name, 
            http_method, 
            resource, 
            default_headers=None, 
            default_params=None,
            default_data=None,
            default_cookies=None, 
            response_transforme=False):
        self.path = path
        self.name = name
        self.http_method = http_method
        self.resource = resource
        self.default_headers = default_headers
        self.default_params = default_params
        self.default_data = default_data
        self.default_cookies = default_cookies
        self.response_transform = response_transforme
        self.transformers = self.resource.api.transformers
        resource.add_endpoint(self)
    
    def get_uri(self):
        api = self.resource.api
        scheme = api.scheme
        authority = api.authority
        return f'{scheme}{authority}{self.path}'
    
    def send_request(self, headers=None, params=None, data=None, cookies=None):
        headers = headers or self.default_headers
        params = params or self.default_params
        data = data or self.default_data
        cookies = cookies or self.default_cookies
        response = getattr(requests, self.http_method.value)(self.get_uri(), headers=headers, params=params, data=data, cookies=cookies)
        print(f'{response.status_code}: [{self.http_method.value}] {self.get_uri()}')
        if self.response_transform:
            response = self.__transform_response(response)
        return response
    
    def __transform_response(self, response):
        resource_transforms = getattr(self.transformers, self.resource.name)
        transform = getattr(resource_transforms, self.name)
        response = transform(response)
        return response

class HTTPMethod(Enum):
    POST = 'post'
    GET = 'get'
    UPDATE = 'update'
    PATCH = 'patch'
    DELETE = 'delete'
    OPTIONS = 'options'
