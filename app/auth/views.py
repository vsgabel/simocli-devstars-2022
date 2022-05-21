from app.auth import auth
from flask import request, flash, make_response, render_template, redirect, url_for

@auth.route("/login", methods=['GET','POST'])
def login():
    dados = request.form
    if dados:
        user = dados['user']
        if user:
            flash("Usuario logado com sucesso")
            resp = make_response(redirect(url_for('main.index')))
            resp.set_cookie('user', user)
            return resp
        flash("Usuario invalido")
    return render_template("login.html", user=request.cookies.get('user'))

@auth.route('/registro')
def registro():
    return render_template("register.html",  user=request.cookies.get('user'))

@auth.route('/logout')
def logout():
    resp = make_response(redirect(url_for("main.index")))
    resp.set_cookie('user', '', expires=0)

    return resp