from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/')
def home():
    return render_template("template.html")
    
#lista personas
@router.route('/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return render_template("nene/lista.html", lista=pd.to_dict())

#Lista personas
@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")\

#Lista personas
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("nene/editar.html", data = nene )

#guardar personas
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)

@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.merge(int(pos) -1)
    return redirect("/personas", code=302)