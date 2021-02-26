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

#@app.route('/', methods=["GET","POST"])
#def index():
#    if(request.method == "POST"):
#        array = ["","","","","\0"]
#        banco = ["B","C","5","2","\0"]
#        array[0] = request.form['var1']
#        array[1] = request.form['var2']
#        array[2] = request.form['var3']
#        array[3] = request.form['var4']
#        clave = concatenar(array, banco)
#        claveRedireccion = ""
#        claveRedireccion = formarString(clave)
#        #print(claveRedireccion)
#        return redirect(f"http://localhost:5000/caja_abierta/{claveRedireccion}")
#    template = env.get_template('index.html')
#    return template.render()
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
                    codigo = 0
                    break
                else:
                    datos = []
                    aviso = "No se encontro una caja relacionada con el código"
                    codigo = 1
        template = env.get_template('index.html')
        return template.render(my_list=datos,textoBoton="Abrir caja: ",mensaje="Ingresar codigo para abrir caja:",aviso=aviso, codigo = codigo)
    template = env.get_template('index.html')
    return template.render(textoBoton="Abrir caja: ",mensaje="Ingresar codigo para abrir caja:", aviso = "")

@app.route('/caja_abierta/<values>', methods=["GET"])
def abierta(values):
    with open('banco.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
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
    codigo = 1
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
    return template.render(textoBoton="Eliminar caja: ",mensaje="Ingresar codigo para eliminar caja:", codigo=codigo) 
@app.route('/LIST')
def listas_cajas():
   return 


@app.route('/Crear_Caja', methods=["GET","POST"])
def Crear_caja():
    if(request.method == "POST"):
        clave = request.form['var1']
        nombre = request.form['var2']
        telefono = request.form['var3']
        direccion = request.form['var4']
        monto = request.form['var5']
        datoscaja = ["","","","",""]
        datoscaja[0] = clave
        datoscaja[1] = nombre
        datoscaja[2] = telefono
        datoscaja[3] = direccion
        datoscaja[4] = monto
        with open('banco.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for rows in reader:
                if(clave == rows[0][0:9]):
                    template = env.get_template('crear.html')
                    return template.render(codigo=1, datoscaja=datoscaja)
        with open('banco.csv', 'a', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter=",",  quotechar=',',quoting=csv.QUOTE_MINIMAL,lineterminator ='')
            writer.writerow('\n')
            writer.writerow(datoscaja) 
          
        template = env.get_template('nuevacaja.html')
        imagen = url_for('static', filename='caja.png') 
        return template.render(datoscaja=datoscaja, imagen=imagen)
    template = env.get_template('crear.html')
    return template.render(codigo = 0)

if __name__ == '__main__':
    app.run()