from flask import Flask
from http import HTTPStatus


app = Flask(__name__)

@app.get("/<string:nome>")
def home(nome):
    return f"<h1>{nome}</h1>", HTTPStatus.OK

app.run(port=5050)
