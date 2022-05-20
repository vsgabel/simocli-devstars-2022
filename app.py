import os
import requests
from flask import Flask, render_template, request, flash, redirect, url_for, make_response

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
app.config['SECRET_KEY'] = 'alguma frase muito segura'

@app.route("/")
def index():
    curitiba = info_cidade('curitiba')
    min_curitiba = float(curitiba['main']['temp_min'])
    atual_curitiba = float(curitiba['main']['temp'])
    max_curitiba = float(curitiba['main']['temp_max'])
    return render_template("index.html", minmax=[min_curitiba, max_curitiba], atual=atual_curitiba, user=request.cookies.get('user'))
    
@app.route("/login", methods=['GET','POST'])
def login():
    dados = request.form
    if dados:
        user = dados['user']
        if user:
            flash("Usuario logado com sucesso")
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('user', user)
            return resp
        flash("Usuario invalido")
    return render_template("login.html", user=request.cookies.get('user'))

@app.route('/registro')
def registro():
    return render_template("register.html",  user=request.cookies.get('user'))

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie('user', '', expires=0)

    return resp

@app.route("/cidades")
def cidades():
    cidades = [
        ["6322752", "Curitiba", "PR/Brasil", -25.504, -49.291, url_for('clima', cidade='6322752')],
        ["3451783", "Realeza", "PR/Brasil", -25.769, -53.532, url_for('clima', cidade='3451783')],
        ["3467400", "Capanema", "PR/Brasil", -53.820, -25.660, url_for('clima', cidade='3467400')],
        ["3454818", "Pato Branco", "PR/Brasil", -26.229, -52.671, url_for('clima', cidade='3454818')],
        ["3470597", "Barra Velha", "PR/Brasil", -26.632, -48.684, url_for('clima', cidade='3470597')],
        ["3455775", "Osasco", "SP/Brasil", -23.532, -46.792, url_for('clima', cidade='3455775')],
        ["3448439", "São Paulo", "SP/Brasil", -23.547, -46.636, url_for('clima', cidade='3448439')],
        ["3451190", "Rio de Janeiro", "RJ/Brasil", -22.903, -43.207, url_for('clima', cidade='3451190')],
        ["6322737", "Colombo", "PR/Brasil", -25.363, -49.185, url_for('clima', cidade='6322737')],
        ["3457967", "Mangueirinha", "PR/Brasil", -25.941, -52.176, url_for('clima', cidade='3457967')],
        ["3585968", "San Salvador", "El Salvador", 13.833, -88.918, url_for('clima', cidade='3585968')],
        ["108410", "Riyadh", "Arábia Saudita", 24.689, 46.722, url_for('clima', cidade='108410')],
        ["2729907", "Longyearbyen", "Svalbard/Noruega", 78.219, 15.640, url_for('clima', cidade='2729907')]
    ]
    return render_template("cidades.html",  user=request.cookies.get('user'), cidades=cidades)

@app.route("/clima/<cidade>")
def clima(cidade):
    dados = info_id(cidade)
    mint = float(dados['main']['temp_min'])
    atual = float(dados['main']['temp'])
    maxt = float(dados['main']['temp_max'])
    nome = dados['name']
    return render_template("clima.html", minmax=[mint, maxt], atual=atual, nome=nome, user=request.cookies.get('user'))


if __name__ == "__main__":
    app.run(debug=True)