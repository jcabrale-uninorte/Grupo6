from os import name
from  flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('Login.html') 

@app.route('/administrador')
def Administardor():
    return render_template('Dashboard.html') 


@app.route('/registro')
def Registrar():
    return render_template('RegistrarUsuario.html')

@app.route('/registro/Perfilusuario')
def Perfil_Usuario():
    return render_template('PerfilUsuario.html')

@app.route('/listapeliculas')
def Lista_Peliculas():
    return render_template('ListadoPeliculas.html')  

@app.route('/login/listadopeliculas/funcion')
def Detalle_funcion():
    return render_template('Detalles.html') 


@app.route('/login/listadopeliculas/busquedad')
def Busquedad():
    return render_template('ResultadoBusquedad.html')
    