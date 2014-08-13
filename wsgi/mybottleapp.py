import logging
import json

from bottle import route, default_app, run, response, abort, post, request

api_version = "5" #API version, please increase by one every time you push
number_storage = {} #storage array for hashes

@route('/')
def index():
    return "HSSPKA API Version: " + api_version

@route('/numbers', method='GET')
def get_numbers():
    number_storage['6274865966'] = 'PUBLICKEY'
    return json.dumps(number_storage.keys())
    
# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'runtime/repo/wsgi/views/')) 

application=default_app()
