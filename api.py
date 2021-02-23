from os import read, truncate
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
            #print(contador)
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
        #print(claveRedireccion)
        return redirect(f"http://localhost:5000/caja_abierta/{claveRedireccion}")
    template = env.get_template('index.html')
    return template.render()
datos = []
aviso = ""
@app.route('/abrir', methods=["GET","POST"])
def indexA():
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
        with open('banco.csv') as File:
            global datos, aviso
            reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if(claveRedireccion == row[0][0:9]):
                    datos = row
                    aviso = ""
                    break
                else:
                    datos = []
                    aviso = "No se encontro"
        template = env.get_template('index.html')
        return template.render(my_list=datos,textoBoton="Abrir caja: ",mensaje="Ingresar codigo para abrir caja:",aviso=aviso)
    template = env.get_template('index.html')
    return template.render(textoBoton="Abrir caja: ",mensaje="Ingresar codigo para abrir caja:", aviso = "")
@app.route('/caja_abierta/<values>', methods=["GET"])
def abierta(values):
    with open('banco.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
            if(values == row[0][0:9]):
                return jsonify(row)
    return "No se encontro"

@app.route('/caja_eliminada/<values>', methods=["GET"])
def eliminada(values):
    nueva = []
    cont = 0
    no = 0
    with open('banco.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for rows in reader:
            if(values == rows[0][0:9]):
                no = cont
                pass
            else:
                nueva.append("")
                cont = cont + 1
    #csv = ["[]","[]","[]","[]"]
    #nueva = ["","",""]
    with open('banco.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        p = 0
        b = 1
        for row in reader:
            print(cont)
            print(row)
            print(no)
            print(p)
            if(p == no and b != 0):
                b = 0
            else:
                nueva[p] = row
                p = p + 1
    with open('banco.csv', 'w', newline="") as writeFile:
        writer = csv.writer(writeFile, delimiter=",",  quotechar=',',quoting=csv.QUOTE_MINIMAL)
        writer.writerows(nueva)
        
    return jsonify(nueva)

@app.route('/DELETE', methods=["GET", "POST"])
def eliminar_caja():
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
        #print(claveRedireccion)
        return redirect(f"http://localhost:5000/caja_eliminada/{claveRedireccion}")
    template = env.get_template('index.html')
    return template.render() 
@app.route('/LIST')
def listas_cajas():
   return 
@app.route('/Crear_Caja')
def Crear_caja(nombre, clave):
    with open('banco.csv', mode='w') as b_file:
        banco_writer = csv.writer(b_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#106 linea para copiar
    #csv = ["[]","[]","[]","[]"]
    #nueva = ["","","",""]
    #despues
    #nueva = ["","","","",""]
    
    return

if __name__ == '__main__':
    app.run()