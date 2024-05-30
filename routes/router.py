import json
import os
from flask import Blueprint, Flask, render_template, request, redirect, url_for
from controls.registro_expresion import registrar_expresion

router = Blueprint('router', __name__)

json_file_path = os.path.join('data', 'expresiones.json')

def cargar_expresiones():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
    return []

def guardar_expresiones(expresiones):
    with open(json_file_path, 'w') as file:
        json.dump(expresiones, file, indent=4)

expresiones_registradas = cargar_expresiones()

@router.route('/')
def index():
    return render_template('index.html')

@router.route('/registrar', methods=['POST'])
def registrar():
    expresion = request.form['expresion']
    expresion_registrada = registrar_expresion(expresion)
    if expresion_registrada:
        expresiones_registradas.append(expresion_registrada)
        guardar_expresiones(expresiones_registradas)
        mensaje = f"Expresión '{expresion}' registrada correctamente."
    else:
        mensaje = f"La expresión '{expresion}' no es correcta"
    return render_template('mensaje.html', mensaje=mensaje)

@router.route('/listar')
def listar():
    return render_template('listar.html', expresiones=expresiones_registradas)
