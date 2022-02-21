from PIL import Image, ImageTk

FUNDO = "#1C1717"
FUNDO_BOTAO = "#551E04"
FUNDO_BOTAO_ATIVO = "#460304"
COR_TEXTO = "#B49A9A"



def frame():
    return {"background": FUNDO}


def label_pergunta():
    return {"background": FUNDO, "foreground": COR_TEXTO, "font": "Georgia 14 bold"}


def label_intro():
    return {"background": FUNDO, "foreground": COR_TEXTO, "font": "Georgia 14", "width": 90}


def label():
    return {"background": FUNDO, "foreground": COR_TEXTO, "font": "Georgia 14"}


def radiobutton():
    return {"background": FUNDO, "activebackground": FUNDO, }


def button():
    return {'background': FUNDO_BOTAO, "foreground": COR_TEXTO, "height": 2, "relief": "flat",
            "font": "Georgia 12 bold", "activebackground": FUNDO_BOTAO_ATIVO, "activeforeground": COR_TEXTO,
            "borderwidth": 0}


