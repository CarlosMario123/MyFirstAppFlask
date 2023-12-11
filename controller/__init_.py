
from flask import Blueprint
from controller.alumnoController import alumnos
# Importaremos todos los Blueprints desde otros archivos


# Registramos los Blueprints en esta sección
def register_blueprints(app):
    #agregamos alumno a registerBluePrint
    app.register_blueprint(alumnos)
 

#