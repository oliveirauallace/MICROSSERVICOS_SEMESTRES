from flask import Flask, request
from flask import jsonify
from pymemcache.client import base

servico = Flask(__name__)

#CONSTANTES

IS_ALIVE = "yes"
VERSION = "0.1"
AUTHOR = "UALLACE OLIVEIRA"
EMAIL = "UALLACE.OLIVEIRAA@GMAIL.COM"
#adicionando o banco volatil
BANCO_VOLATIL = "banco_volatil"


#rotas do meu servico
#Rota de ping perguntando o servico se ele esta atendendo
@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE

#Rota que informa informações basicas sobre o servico e criador do servicos
@servico.route("/info/")
def get_info():
    info = jsonify(
        version = VERSION,
        author = AUTHOR,
        email = EMAIL
    )

    return info

@servico.route("/gravar/", methods=["post", "get"])
def gravar():
    grade = request.get_json()
    if grade:
        cliente = base.Client((BANCO_VOLATIL, 11211))
        cliente.set("sexto", grade)

        cliente.close()

    return "OK"

@servico.route("/grade/")
def get_sexto_semestre():
    cliente = base.Client((BANCO_VOLATIL, 11211))
    grade = cliente.get("sexto")
    cliente.close()

    return grade

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )