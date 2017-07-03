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

class APIConfig():
    def __init__(self, key):
        self.key = key

    def __call__(self, project):
        print "Package %s" % project
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

        result = {
            'error': None
        }

        try:
            content = out.json()
        except ValueError:
            content = out._content

        result['is_deprecated'] = (out.headers['X-Build-Deprecated'] == 'true')

        if result['is_deprecated']:
            service = self.project
            version = out.headers['X-Build-Version']
            console.warn('%s v%s is deprecated! Run `api update %s` to use the latest version' % (
                service, version, service
            ))

        if out.status_code > 299:
            result['error'] = content
            content = None
            console.error(result['error']['error'])

        return content, result
