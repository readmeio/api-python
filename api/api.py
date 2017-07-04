#!/usr/bin/env python
import json
import requests
from requests.auth import HTTPBasicAuth

class console:
    @staticmethod
    def error(text):
        print '\033[91m' + text + '\033[0m'
    @staticmethod
    def warn(text):
        print '\033[93m' + text + '\033[0m'

def config(key):
    return api(key)

class api():
    def __init__(self, key):
        self.key = key

    def __call__(self, project):
        request = Request(project=project, key=self.key)
        return request

class Request():
    def __init__(self, project, key):
        self.project = project
        self.key = key

    def run(self, method, data):
        out = requests.post('https://api.readme.build/services/%s/%s/invoke' % (self.project, method),
            data=data,
            auth=HTTPBasicAuth(self.key, '')
            )

        result = Response()

        try:
            content = out.json()
        except ValueError:
            content = out._content

        result.is_deprecated = (out.headers.setdefault('X-Build-Deprecated', 'false') == 'true')

        if result.is_deprecated:
            service = self.project
            version = out.headers['X-Build-Version']
            console.warn('%s v%s is deprecated! Run `api update %s` to use the latest version' % (
                service, version, service
            ))

        if out.status_code > 299:
            result.error = content
            content = None
            console.error(result.error['error'])

        return content, result

class Response():
    def __init__(self, error=None, is_deprecated=False):
        self.error = error
        self.is_deprecated = is_deprecated

