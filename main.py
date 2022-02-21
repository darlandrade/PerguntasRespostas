import json
import random
from tkinter import messagebox

from arquivo_perguntas import perguntas
from arquivo_alternativas import alternativas
from arquivo_respostas import respostas
from tkinter import *
from constantes import frame, label, label_pergunta, radiobutton, button, label_intro


class Perguntas_Respostas(Tk):
    def __init__(self):
        Tk.__init__(self)
        x = 800
        y = 800
        self.geometry(f"{x}x{y}")
        self.config(frame())
        self.title("Perguntas e respostas - Que comecem os jogos")

        # Frame introdução
        f_introducao = Frame(self, frame())
        f_introducao.pack()
        self.introducao = "O jogo é simples, não existe limite de acertos. Temos 70 perguntas\n" \
                          " e você pode ir até o fim caso vá acertando, porém, caso erre 5x,\n" \
                          " o jogo será encerrado."
        l_introducao = Label(f_introducao, text=self.introducao, **label_intro())
        l_introducao.pack()

        # Frame para as perguntas
        f_perguntas = Frame(self, frame())
        f_perguntas.pack()

        # Perguntas
        self.l_pergunta = Label(f_perguntas, **label_pergunta())
        self.l_pergunta.pack()

        f_alternativas = Frame(self, frame())
        f_alternativas.pack()
        # Alternativas
        self.alternativa_op = StringVar(value="a")
        self.img_1 = PhotoImage(file="./images/selected.png")
        self.img_2 = PhotoImage(file="./images/notselected.png")
        self.c_alternativa_a = Radiobutton(f_alternativas, variable=self.alternativa_op, value="a", **radiobutton())
        self.c_alternativa_b = Radiobutton(f_alternativas, variable=self.alternativa_op, value="b", **radiobutton())
        self.c_alternativa_c = Radiobutton(f_alternativas, variable=self.alternativa_op, value="c", **radiobutton())
        self.c_alternativa_d = Radiobutton(f_alternativas, variable=self.alternativa_op, value="d", **radiobutton())
        self.c_alternativa_e = Radiobutton(f_alternativas, variable=self.alternativa_op, value="e", **radiobutton())

        self.c_alternativa_a.grid(row=0, column=0)
        self.c_alternativa_b.grid(row=1, column=0)
        self.c_alternativa_c.grid(row=2, column=0)
        self.c_alternativa_d.grid(row=3, column=0)
        self.c_alternativa_e.grid(row=4, column=0)

        self.l_alternativa_a = Label(f_alternativas, **label())
        self.l_alternativa_b = Label(f_alternativas, **label())
        self.l_alternativa_c = Label(f_alternativas, **label())
        self.l_alternativa_d = Label(f_alternativas, **label())
        self.l_alternativa_e = Label(f_alternativas, **label())


        self.l_alternativa_a.grid(row=0, column=1, pady=(5, 0))
        self.l_alternativa_b.grid(row=1, column=1, pady=(5, 0))
        self.l_alternativa_c.grid(row=2, column=1, pady=(5, 0))
        self.l_alternativa_d.grid(row=3, column=1, pady=(5, 0))
        self.l_alternativa_e.grid(row=4, column=1, pady=(5, 0))

        # Checar resposta
        f_check_answer = Frame(self, frame())
        f_check_answer.pack()

        self.b_valida_resposta = Button(f_check_answer, text='Verificar reposta', **button(),
                                        command=self.set_label_pergunta_text)
        self.b_valida_resposta.pack(pady=10)

        # Frame para a pontuação
        f_pontuacao = Frame(self, frame())
        f_pontuacao.pack()

        self.pontuacao = 0
        self.l_pontuacao = Label(f_pontuacao, text="Pontos: 0", **label())
        self.l_pontuacao.pack()
        self.l_erros = Label(f_pontuacao, **label())
        self.l_erros.pack()
        self.tentativas = 6
        # Frame para a resposta
        f_resposta = Frame(self, frame())
        f_resposta.pack()

        # Variável para armazenar a pergunta que já foi
        self.todas_perguntas = list(perguntas().items())
        self.todas_alternativas = alternativas()
        self.todas_respostas = respostas()
        self.set_label_pergunta_text()
        # self.escolhas_numeros = [n for n in range(1, 71)]

    def set_label_pergunta_text(self):
        escolha = random.choice(self.todas_perguntas)
        self.l_pergunta['text'] = escolha[1]
        self.todas_perguntas.remove(escolha)
        alternatives = self.get_alternatives(escolha[0])
        self.l_alternativa_a['text'] = alternatives[0]
        self.l_alternativa_b['text'] = alternatives[1]
        self.l_alternativa_c['text'] = alternatives[2]
        self.l_alternativa_d['text'] = alternatives[3]
        self.l_alternativa_e['text'] = alternatives[4]

        resposta = self.get_resposta(escolha[0])

        if self.alternativa_op.get() == "a" and resposta[1:2] == "a":
            self.pontuacao += 1
        elif self.alternativa_op.get() == "b" and resposta[1:2] == "b":
            self.pontuacao += 1
        elif self.alternativa_op.get() == "c" and resposta[1:2] == "c":
            self.pontuacao += 1
        elif self.alternativa_op.get() == "d" and resposta[1:2] == "d":
            self.pontuacao += 1
        elif self.alternativa_op.get() == "e" and resposta[1:2] == "e":
            self.pontuacao += 1
        else:
            self.tentativas -= 1
            if self.tentativas == 0:
                messagebox.showinfo("Fim de jogo", "Você esgotous suas tentativas, o jogo será finalizado.")
                self.quit()
            elif self.tentativas == 6:
                self.l_erros['text'] = ""
            else:
                f"Errado, você tem mais {self.tentativas} tentativas"

        self.l_pontuacao['text'] = f"Pontos: {self.pontuacao}"

        del self.todas_alternativas[escolha[0]]

    def get_alternatives(self, question_number):
        alternatives = self.todas_alternativas.get(question_number)
        posicoes = []
        for i, v in enumerate(alternatives):
            if ")" == v:
                posicoes.append(int(i+2))

        a = alternatives[posicoes[0]:posicoes[1]-4]
        b = alternatives[posicoes[1]:posicoes[2]-4]
        c = alternatives[posicoes[2]:posicoes[3]-4]
        d = alternatives[posicoes[3]:posicoes[4]-4]
        e = alternatives[posicoes[4]:]

        return a, b, c, d, e

    def get_resposta(self, escolha):
        return self.todas_respostas.get(escolha)


if __name__ == '__main__':
    perguntas_respostas = Perguntas_Respostas()
    perguntas_respostas.mainloop()


