from app import app
from flask import render_template, redirect, url_for, request, flash
from app.forms import ContatoForm


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

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        nome = form.nome.data #pega o valor do campo 'nome' no form
        email = form.email.data 
        mensagem = form.mensagem.data
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for("contato"))
    return render_template("contato.html", form=form)

@app.route("/entrar", methods=['GET', 'POST'])
def entrar():
    msg = ''
    if request.method == 'POST':
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario == 'admin' and senha == 'admin':
            return redirect(url_for('usuario', nome=usuario))
        else:
            msg = 'Usuario ou senhas incorretos'
    return render_template("entrar.html", msg=msg)
