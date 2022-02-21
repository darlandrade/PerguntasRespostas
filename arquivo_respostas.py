import json


def respostas():
    with open("./arquivos/Respostas.json", "r", encoding="utf8") as arquivo:
        dict_respostas = json.load(arquivo)
        return dict_respostas

