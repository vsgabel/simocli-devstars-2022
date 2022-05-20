import os
import requests
from flask import Flask, render_template, request, flash, redirect, url_for

api_key = os.environ.get("WEATHER_API") or None
if not api_key:
    raise Exception("API Key not found")

def info_cidade(cidade):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return resp.json()

def info_id(id):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={id}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return resp.json()

app = Flask(__name__)

@app.route("/")
def index():
    curitiba = info_cidade('curitiba')
    min_curitiba = float(curitiba['main']['temp_min'])
    atual_curitiba = float(curitiba['main']['temp'])
    max_curitiba = float(curitiba['main']['temp_max'])
    return render_template("index.html", minmax=[min_curitiba, max_curitiba], atual=atual_curitiba)
    
@app.route("/login", methods=['GET','POST'])
def login():
    dados = request.form
    if dados:
        user = dados['user']
        if user:
            flash("Usuario logado com sucesso")
            return redirect(url_for('index'))
        flash("Usuario invalido")
    return render_template("login.html")

@app.route('/registro')
def registro():
    return render_template("register.html")

@app.route("/cidades")
def cidades():
    return render_template("cidades.html")

@app.route("/clima/<cidade>")
def clima(cidade):
    dados = info_id(cidade)
    mint = float(dados['main']['temp_min'])
    atual = float(dados['main']['temp'])
    maxt = float(dados['main']['temp_max'])
    nome = dados['name']
    return render_template("clima.html", minmax=[mint, maxt], atual=atual, nome=nome)


if __name__ == "__main__":
    app.run(debug=True)