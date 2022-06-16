import requests
import json
from time import sleep


PRIMEIRO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/primeiro.json"
SEGUNDO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/segundo.json"
TERCEIRO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/terceiro.json"
QUARTO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/quarto.json"
QUINTO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/quinto.json"
SEXTO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/sexto.json"
SETIMO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/setimo.json"
OITAVO_SEMESTRE = "/home/Uallace/Documents/SDI/Uallace Oliveira Silva/versao4/grade/oitavo.json"

URL_SERVICO_PRIMEIRO_SEMESTRE = "http://localhost:5001/gravar/"
URL_SERVICO_SEGUNDO_SEMESTRE = "http://localhost:5002/gravar/"
URL_SERVICO_TERCEIRO_SEMESTRE = "http://localhost:5003/gravar/"
URL_SERVICO_QUARTO_SEMESTRE = "http://localhost:5004/gravar/"
URL_SERVICO_QUINTO_SEMESTRE = "http://localhost:5005/gravar/"
URL_SERVICO_SEXTO_SEMESTRE = "http://localhost:5006/gravar/"
URL_SERVICO_SETIMO_SEMESTRE = "http://localhost:5007/gravar/"
URL_SERVICO_OITAVO_SEMESTRE = "http://localhost:5008/gravar/"

def enviar(url, json_grade):
    with open(json_grade, "r") as arquivo:
        grade = json.load(arquivo)
        arquivo.close()

        resposta = requests.post(url, json=json.dumps(grade))
        if resposta.ok:
            resposta = "Informacoes de Grade do Curso de BSI Enviadas"
        else:
            resposta = "Erro no envio" + resposta.text

        return resposta

if __name__ == "__main__":
    while True:        
        resposta = enviar(URL_SERVICO_PRIMEIRO_SEMESTRE, PRIMEIRO_SEMESTRE)
        print(f"enviei informacoes do primeiro semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_SEGUNDO_SEMESTRE, SEGUNDO_SEMESTRE)
        print(f"enviei informacoes do segundo semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_TERCEIRO_SEMESTRE, TERCEIRO_SEMESTRE)
        print(f"enviei informacoes do terceiro semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_QUARTO_SEMESTRE, QUARTO_SEMESTRE)
        print(f"enviei informacoes do qiuarto semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_QUINTO_SEMESTRE, QUINTO_SEMESTRE)
        print(f"enviei informacoes do quinto semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_SEXTO_SEMESTRE, SEXTO_SEMESTRE)
        print(f"enviei informacoes do sexto semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_SETIMO_SEMESTRE, SETIMO_SEMESTRE)
        print(f"enviei informacoes do setimo semestre. Resultado: {resposta}")

        resposta = enviar(URL_SERVICO_OITAVO_SEMESTRE, OITAVO_SEMESTRE)
        print(f"enviei informacoes do oitavo semestre. Resultado: {resposta}")

        
        sleep(10)

