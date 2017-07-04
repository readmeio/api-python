from unittest import TestCase

import api

class TestAPI(TestCase):
    def hello(self):
        s = api.lorem()
        self.assertTrue(isinstance(s, basestring))
