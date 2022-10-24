from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioUsuario
from models import Usuarios

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/logoff')
def logoff():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
            if form.senha.data == usuario.senha:
                session['usuario_logado'] = usuario.nickname
                flash(usuario.nickname + ' logado com sucesso!')
                proxima_pagina = request.form['proxima']
                if proxima_pagina == 'None':
                    return redirect(url_for('index'))
                return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))
