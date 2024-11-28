from flask import Flask, Blueprint, jsonify, abort, request
from server import app

v1_parent_bp = Blueprint('v1_parent_bp',__name__, url_prefix="/")
#from server.routes import no_token
#from server.routes import empleados

from server.routes.personas import home
v1_parent_bp.register_blueprint(home)

from server.routes.chat import chat
v1_parent_bp.register_blueprint(chat)

app.register_blueprint(v1_parent_bp)