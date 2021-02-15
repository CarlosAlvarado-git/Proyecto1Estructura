from flask import Flask, url_for, request, redirect, jsonify
from jinja2 import Template, Environment, FileSystemLoader
import csv
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)

def concatenar(user, banco):
    clave = ["","","","","","","","","", ""]
    contador = 0
    for i in user:
        if i != "\0":
            print(contador)
            clave[contador] = i
            contador += 1
    clave[contador] = "-" 
    contador += 1       
    for i in banco:
        if i != "\0":
            clave[contador] = i
            contador += 1
    clave[contador] = "\0"
    return clave

def formarString(clave):
    string = ""
    clave = clave[:-1]
    for i in clave:
        string += i
    return string

@app.route('/', methods=["GET","POST"])
def index():
    if(request.method == "POST"):
        array = ["","","","","\0"]
        banco = ["B","C","5","2","\0"]
        array[0] = request.form['var1']
        array[1] = request.form['var2']
        array[2] = request.form['var3']
        array[3] = request.form['var4']
        clave = concatenar(array, banco)
        claveRedireccion = ""
        claveRedireccion = formarString(clave)
        print(claveRedireccion)
        return redirect(f"http://localhost:5000/caja_abierta/{claveRedireccion}")
    template = env.get_template('index.html')
    return template.render()

@app.route('/caja_abierta/<values>', methods=["GET"])
def abierta(values):
    with open('banco.csv') as File:
        reader = csv.reader(File, delimiter=';', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if(values == row[0][0:9]):
                return jsonify(row)
    return "No se encontro"

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
def Crear_caja(nombre, clave):
    with open('banco.csv', mode='w') as b_file:
        banco_writer = csv.writer(b_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    return

if __name__ == '__main__':
    app.run()