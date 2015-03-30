from flask import Flask
from flask import current_app, request
from flask.ext.login import LoginManager
import requests
from models import User

app = Flask(__name__, static_folder=None)
app.url_map.strict_slashes = False
app.config.from_pyfile('config.py')
try:
  app.config.from_pyfile('local_config.py')
except IOError:
  pass

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.request_loader
def load_user_from_request(request):

    user = None
    
    # try to login using User header
    user_key = request.headers.get('User') or 'Anonymous'
    if user_key:
        user = User.query.filter_by(key=user_key).first()
        if user:
            return user
        else:
            # create a new user
            return User(key=user_key)

    # finally, return Anonymous
    return None

@app.route('/library/<operation>', methods=['GET'])
def library(operation):
    '''Access point for library operations'''
    return '{}', 200

def check_request(request):
    
    headers = dict(request.headers)
    if 'Orcid-Authorization' not in headers:
        raise Exception('Header Orcid-Authorization is missing')
    h = {
         'Accept': 'application/json', 
         'Authorization': headers['Orcid-Authorization'],
         'Content-Type': 'application/json'
         }
    # transfer headers from the original
    #for x in ['Content-Type']:
    #    if x in headers:
    #        h[x] = headers[x]
            
    if 'Content-Type' in headers \
        and headers['Content-Type'] == 'application/json' \
        and request.method in ('POST', 'PUT'):
        payload = request.json
    else:
        payload = dict(request.args)
        payload.update(dict(request.form))
    
    return (payload, h)

