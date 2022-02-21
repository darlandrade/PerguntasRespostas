import json


def perguntas() -> dict:
    with open("./arquivos/Perguntas.json", "r", encoding="utf8") as arquivo:
        dict_perguntas = json.load(arquivo)
        return dict_perguntas


if __name__ == '__main__':
    perguntas()
