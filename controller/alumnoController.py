from flask import Blueprint,jsonify
from data.alumnos import sendAll

#crearemos los blueprint para alumnos
alumnos = Blueprint('alumnos', __name__)

#esta ruta mandara todos los alumnos
@alumnos.route("/alumnos")
def getAll():
    return jsonify(sendAll())


@alumnos.route("/alumnos/<int:id>")
def getById(id):
    alumno_encontrado = None
    for alumno in sendAll():
        if alumno["id"] == id:
            alumno_encontrado = alumno
            break
    
    if alumno_encontrado:
        return jsonify(alumno_encontrado)
    else:
        return jsonify({"mensaje": "Alumno no encontrado"}), 404  # Devolver un mensaje si el alumno no existe
    