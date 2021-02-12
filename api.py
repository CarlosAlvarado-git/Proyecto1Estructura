from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
import yaml
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)
with open("banco.yaml") as yaml_file:
    datos_banco = yaml.load(yaml_file)

def concatenar(user, banco):

    return 

@app.route('/', methods=["POST"])
def index():
    if(request.method == "POST"):
        array = ["","","","","\0"]
        array[0] = request.form['var1']
        array[1] = request.form['var2']
        array[2] = request.form['var3']
        array[3] = request.form['var4']
    return 
@app.route('/cajaabierta/<values>', methods=["GET"])
def caja():

   return
@app.route('/DELETE', methods=["GET", "POST"])
def eliminar_caja():
   return 
@app.route('/LIST')
def listas_cajas():
   return 

if __name__ == '__main__':
    app.run()