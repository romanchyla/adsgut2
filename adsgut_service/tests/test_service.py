import sys, os
from urllib import urlencode
PROJECT_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(PROJECT_HOME)
from flask.ext.testing import TestCase
from flask import url_for, request
import unittest
import json
import httpretty
import cgi
from StringIO import StringIO
from stubdata import orcid_profile

class TestServices(TestCase):
    '''Tests that each route is an http response'''

    def create_app(self):
        '''Start the wsgi application'''
        from views import app
        return app.create_app()


    def test_access(self):
        '''Allows access based on permissions'''
        pass
        
if __name__ == '__main__':
  unittest.main()
