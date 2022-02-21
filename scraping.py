import json

import requests as r
from bs4 import BeautifulSoup as bs

url = "https://www.todamateria.com.br/perguntas-e-respostas-de-conhecimentos-gerais/"

con = r.get(url)
bs4 = bs(con.content, "html.parser")

perguntas = bs4.findAll("h2")

# ==================== #
# with open("Perguntas.json", 'w', encoding="utf8") as arquivo:
#     lista_de_perguntas = []
#     for p in perguntas[:70]:
#         lista_de_perguntas.append(p.text.split(". "))
#
#     perguntas = {}
#     for item in lista_de_perguntas:
#         perguntas[f"{item[0]}"] = item[1]
#
#     obj = json.dumps(perguntas, ensure_ascii=False)
#     arquivo.write(obj)
# ==================== #

# alternativas = bs4.findAll("p")
# # contagem = [a for a in alternativas[2:]]
#
# lista_alternativas = []
# for a in alternativas[2:]:
#     if "a) " in a.text:
#         lista_alternativas.append(a.text)
#
# with open("Alternativas.json", "w", encoding="utf8") as arquivo:
#     gravar = {}
#     for indice, alt in enumerate(lista_alternativas):
#         gravar[f"{indice+1}"] = alt
#
#     obj = json.dumps(gravar, ensure_ascii=False)
#     arquivo.write(obj)
# ==================== #
# respostas = bs4.findAll("div", {"class": "answer-contents"})
# with open("arquivos/Respostas.json", "w", encoding="utf8") as arquivo:
#     gravar = {}
#     for indice, r in enumerate(respostas):
#         gravar[f"{indice+1}"] = r.p.text.strip("Alternativa")
#
#     obj = json.dumps(gravar, ensure_ascii=False)
#     arquivo.write(obj)
