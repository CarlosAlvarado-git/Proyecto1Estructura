from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
import csv
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)
with open("banco.csv") as File:
    datos_banco = csv.reader(File)

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
@app.route('/caja_abierta/<values>', methods=["GET"])
def abierta():

   return
@app.route('/caja_eliminada/<values>', methods=["GET"])
def eliminada():

   return
@app.route('/DELETE', methods=["GET", "POST"])
def eliminar_caja():
   return 
@app.route('/LIST')
def listas_cajas():
   return 
@app.route('/Crear_Caja')
def Crear_caja():
    with open('banco.csv', mode='w') as b_file:
        banco_writer = csv.writer(b_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    return

if __name__ == '__main__':
    app.run()