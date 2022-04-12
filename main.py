from jinja2 import Environment
from jinja2 import FileSystemLoader
from flask import Flask
from flask import render_template
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)


@app.route('/tittle')
def tittle():
    return render_template('tittle.html', tittle='Slang Panameño')
@app.route('/name')
def name():
    return render_template('name.html', name='JOSE DONDIS')
@app.route('/cedula')
def cedula():
    return render_template('cedula.html', cedula='4-812-1989')
@app.route('/palabra')
def palabra1():
    palabras_favoritas =["Mopri: Significa primo.", "Ofi/Ofe: Significa Si.", "Chantin: Significa casa.", "Nave: Significa carro.", "Tongo: Significa policia.", "Congo: Significa una persona tonta.", 41]
    return render_template('palabra1.html')
@app.route('/palabra')
def palabra2():
    return render_template('palabra2.html', palabra2='Ofi/Ofe', significado2='Significa Si')
