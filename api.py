from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)

@app.route('/linear/<int:N>/<int:Values>', methods=['GET'])
def linea_search(N=None,Values=None):
    return 

@app.route('/binary/<int:N>/<int:Values>', methods=['GET'])
def binary_search(N=None,Values=None):
   return 

if __name__ == '__main__':
    app.run()