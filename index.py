from flask import Flask, render_template
from controller.__init_ import register_blueprints

app = Flask(__name__)

#pasamos app aca para darle todos los blueprint
register_blueprints(app)


@app.route('/')
def index():
    #por predeterminado buscara en la carpeta templates
    return render_template("inicio.html")




if __name__ == '__main__':
    app.run(debug=True)
