import requests

def info_cidade(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return resp.json()

def info_id(id, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={id}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return resp.json()