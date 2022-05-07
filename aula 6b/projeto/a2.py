from flask import Flask
from http import HTTPStatus
import requests

app = Flask(__name__)

# Endpoint
@app.get("/<string:nome>")
def home(nome):
    #return f"<h1>{nome}</h1>",HTTPStatus.OK
    if nome != "cavalo":
        return {"msg": f"O valor {nome} que você passou não é valido"}, HTTPStatus.BAD_REQUEST
    else:
        return {"msg": "Seja bem-vindo ao clã. Cavalos codififcadores!"}

app.run(port=5000)