from flask import (
    Flask, 
    request,
    Blueprint,
    jsonify
)
from flask_cors import CORS


#from flask_bcrypt import Bcrypt

#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address

#from flask_mail import Mail

import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
app.config.from_object(os.getenv('SERVER_CONFIGURATION', None))

app.app_context().push()

# SQLALCHEMY DB SET UP 
#db=SQLAlchemy(app)

# BCRYPT
#bcrypt=Bcrypt(app)

# MIGRATION
#migrate = Migrate(app,db)

# MAIL
#mail = Mail(app)
#app.extensions['mail'].debug = 0

# CORS
CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":{'origins':"http://localhost:8080","allow_headers":"Access-Control-Allow-Origin"}})

# REQUESTS LIMITER
#def get_client_ip():
#    return request.headers.get('X-Forwarded-For', get_remote_address)
#
#limiter = Limiter(app=app,key_func=get_client_ip)

# request handler
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
    return response


from server import routes
