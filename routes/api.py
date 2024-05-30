from flask import Blueprint, jsonify, make_response, request
from models.pila import Pila
from controls.expresion_aritmetica import expresion_aritmetica
from controls.listar_expresiones import listar_expresiones

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return make_response(jsonify({"msg": "OK", "code": 200}), 200)

@api.route('/expresiones', methods=["GET"])
def lista_expresiones():
    expresiones = listar_expresiones()
    return jsonify(expresiones)

@api.route('/expresiones/registrar', methods=["POST"])
def registrar_expresiones():
    data = request.json
    if not all(key in data for key in ['expresion']):
        return make_response(jsonify({"msg": "Faltan datos", "code": 400}), 400)

    resultado = expresion_aritmetica(data['expresion'])
    return jsonify({"expresion": data['expresion'], "resultado": resultado})
