import json


def alternativas() -> dict:
    with open("./arquivos/Alternativas.json", "r", encoding="utf8") as arquivo:
        dict_alternativas = json.load(arquivo)
        return dict_alternativas
