import base64

from infobip.util.exception import ApiException, ApiRequestError, ApiRequestErrorDetails

__author__ = 'mstipanov'

import http.client
import urllib.request, urllib.parse, urllib.error
import json
from urllib.parse import urlparse


class HttpClient:
    def deserialize(self, s, cls):
        vals = json.JSONDecoder().decode(s)
        return self.deserialize_map(vals, cls)

    def deserialize_map(self, vals, cls):
        obj = cls()

        if not hasattr(vals, 'items'):
            return vals

        for key, val in list(vals.items()):
            t = type(getattr(obj, key, None))
            value = self.deserialize_map(val, t)
            setattr(obj, key, value)

        return obj

    def serialize(self, body_object):
        return body_object.to_JSON()

    def get_value(self, http_method, configuration, method_path, path_params, context, body_object, value_type):
        if path_params:
            for key, value in path_params.items():
                method_path = method_path.replace("{" + key + "}", str(value))

        url = configuration.base_url + method_path
        username = configuration.username
        password = configuration.password
        api_key = configuration.api_key
        token = configuration.token

        if context:
            if isinstance(context, dict):
                params = urlparse(context)
            else:
                params = urlparse(context.to_dict())
            url += "?%s" % params

        u = urlparse(url)
        if u.scheme == "https":
            connection = http.client.HTTPSConnection(u.netloc)
        else:
            connection = http.client.HTTPConnection(u.netloc)

        headers = {}
        if username:
            auth = base64.encodebytes('%s:%s' % (username, password)).replace('\n', '')
            headers["Authorization"] = "Basic %s" % auth

        if api_key:
            headers["Authorization"] = "ApiKey %s" % api_key

        if token:
            headers["Authorization"] = "IBSSO %s" % token

        body_content = None
        if body_object:
            body_content = self.serialize(body_object)
            headers["Accept"] = "application/json"

        headers["Content-Type"] = "application/json"
        headers["User-Agent"] = "Python-Client-Library"

        connection.request(http_method, url, body_content, headers)
        response = connection.getresponse()

        status_code = response.status
        response_content = response.read()
        if status_code < 200 or status_code >= 300:
            content_type = response.getheader("Content-Type")
            if content_type and content_type.startswith("application/json"):
                raise self.deserialize(response_content, ApiException)

            raise ApiException(
                ApiRequestError(None, ApiRequestErrorDetails(response.reason + " - " + response_content)))

        content_type = response.getheader("Content-Type")
        if content_type and content_type.startswith("application/json") and not str == value_type:
            return value_type.from_JSON(response_content)

        return response_content
