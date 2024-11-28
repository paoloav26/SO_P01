from flask import Flask, Blueprint, jsonify, abort, request, render_template

import os
from dotenv import load_dotenv

load_dotenv()


home = Blueprint('home',__name__)

def verificador(arr):
    for item in arr:
        if item == None:
            return False
    return True

# ESTA ES LA WEBADA POR IMPLEMENTADA DE LA VIDA

@home.route("/", methods=["GET"])
def get_home_index():
    return render_template(f'index.html')

@home.route("/<persona>", methods=["GET"])
def get_persona(persona):
    return render_template(f'{persona}.html')

@home.route("/generador", methods=["GET"])
def get_generador():
    return render_template(f'imagenes.html')