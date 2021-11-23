from app import app
from flask import render_template, redirect, url_for


@app.route('/')  
def index():    
   return render_template("index.html")    
  
@app.route('/usuario/<nome>') 
def usuario(nome): 
    return render_template("usuario.html", nome = nome)

@app.route('/boletim')
def boletim():
    notas = {'portugues':5,'matematica':6,'fisica':7}
    return render_template("boletim.html", boletim = notas)

@app.route('/nota/<int:valor>')
def nota(valor):
    return render_template("nota.html", nota = valor)