from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)

@app.route('/')
def index():
    return 

@app.route('/OPEN')
def abrir_caja():
   return 
@app.route('/DELETE')
def eliminar_caja():
   return 
@app.route('/LIST')
def listas_cajas():
   return 

if __name__ == '__main__':
    app.run()