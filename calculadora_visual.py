import customtkinter as ctk
import numpy as np
import sympy as sp
from scipy import special

# CONFIGURAÇÃO DA JANELA

app = ctk.CTk()

app.title("Calculadora Científica")
app.geometry("500x700")

# MEMÓRIA

mem = {"valor": 0.0}

# TELA

tela = ctk.CTkEntry(
    app,
    width=440,
    height=60,
    font=("Arial", 28),
    justify="right"
)

tela.pack(pady=20)

# FUNÇÕES BÁSICAS


def clique_botao(texto):
    tela.insert("end", texto)


def limpar():
    tela.delete(0, "end")


def apagar():
    valor = tela.get()
    tela.delete(0, "end")
    tela.insert("end", valor[:-1])


def calcular():
    try:
        expressao = tela.get()
        resultado = eval(expressao)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")

# FUNÇÕES CIENTÍFICAS

def raiz_quadrada():
    try:
        numero = float(tela.get())
        resultado = np.sqrt(numero)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def raiz_cubica():
    try:
        numero = float(tela.get())
        resultado = np.cbrt(numero)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def logaritmo():
    try:
        numero = float(tela.get())
        resultado = np.log(numero)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def fatorial():
    try:
        numero = int(float(tela.get()))
        resultado = special.factorial(numero, exact=True)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def trigonometria():
    try:
        numero = float(tela.get())
        angulo = np.radians(numero)

        seno = np.sin(angulo)
        cosseno = np.cos(angulo)
        tangente = np.tan(angulo)

        tela.delete(0, "end")
        tela.insert(
            "end",
            f"sen={seno:.4f} cos={cosseno:.4f} tan={tangente:.4f}"
        )

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def mdc():
    try:
        numeros = list(map(int, tela.get().split()))

        resultado = np.gcd.reduce(numeros)

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def media_desvio():
    try:
        numeros = np.array(tela.get().split(), dtype=float)

        media = np.mean(numeros)
        desvio = np.std(numeros)

        tela.delete(0, "end")
        tela.insert(
            "end",
            f"m={media:.2f} d={desvio:.2f}"
        )

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


# =========================
# SYMPY
# =========================

def derivada():
    try:
        funcao = ctk.CTkInputDialog(
            text="Digite a função usando x:",
            title="Derivada"
        ).get_input()

        x = sp.Symbol("x")

        resultado = sp.diff(
            sp.sympify(funcao),
            x
        )

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def integral():
    try:
        funcao = ctk.CTkInputDialog(
            text="Digite a função usando x:",
            title="Integral"
        ).get_input()

        x = sp.Symbol("x")

        resultado = sp.integrate(
            sp.sympify(funcao),
            x
        )

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def equacao():
    try:
        funcao = ctk.CTkInputDialog(
            text="Digite a equação usando x:",
            title="Equação"
        ).get_input()

        x = sp.Symbol("x")

        resultado = sp.solve(
            sp.sympify(funcao),
            x
        )

        tela.delete(0, "end")
        tela.insert("end", str(resultado))

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def porcentagem():
    try:
        total = float(
            ctk.CTkInputDialog(
                text="Digite o total:",
                title="Porcentagem"
            ).get_input()
        )

        parte = float(
            ctk.CTkInputDialog(
                text="Digite a parte:",
                title="Porcentagem"
            ).get_input()
        )

        resultado = (parte / total) * 100

        tela.delete(0, "end")
        tela.insert("end", f"{resultado:.2f}%")

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


# MEMÓRIA

def memoria_mais():
    try:
        mem["valor"] += float(tela.get())
        limpar()

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def memoria_menos():
    try:
        mem["valor"] -= float(tela.get())
        limpar()

    except Exception:
        tela.delete(0, "end")
        tela.insert("end", "Erro")


def memoria_recuperar():
    tela.delete(0, "end")
    tela.insert("end", str(mem["valor"]))


def memoria_limpar():
    mem["valor"] = 0.0


# FRAME DOS BOTÕES

frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

# BOTÕES PRINCIPAIS


botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for linha, botoes_linha in enumerate(botoes):

    for coluna, texto in enumerate(botoes_linha):

        if texto == "=":
            comando = calcular
        else:
            comando = lambda t=texto: clique_botao(t)

        btn = ctk.CTkButton(
            frame_botoes,
            text=texto,
            width=85,
            height=55,
            font=("Arial", 20),
            command=comando
        )

        btn.grid(
            row=linha,
            column=coluna,
            padx=5,
            pady=5
        )
# BOTÕES DE CONTROLE


frame_controle = ctk.CTkFrame(app)
frame_controle.pack(pady=5)

ctk.CTkButton(
    frame_controle,
    text="C",
    width=85,
    height=45,
    command=limpar
).grid(row=0, column=0, padx=5, pady=5)

ctk.CTkButton(
    frame_controle,
    text="⌫",
    width=85,
    height=45,
    command=apagar
).grid(row=0, column=1, padx=5, pady=5)

# BOTÕES CIENTÍFICOS

frame_cientifico = ctk.CTkFrame(app)
frame_cientifico.pack(pady=10)

cientificos = [
    ("√", raiz_quadrada),
    ("∛", raiz_cubica),
    ("ln", logaritmo),
    ("n!", fatorial),
    ("sen/cos/tan", trigonometria),
    ("MDC", mdc),
    ("Média", media_desvio),
    ("%", porcentagem),
    ("d/dx", derivada),
    ("∫", integral),
    ("Equação", equacao)
]

for i, (texto, comando) in enumerate(cientificos):

    btn = ctk.CTkButton(
        frame_cientifico,
        text=texto,
        width=120,
        height=45,
        command=comando
    )

    btn.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )
# MEMÓRIA

frame_memoria = ctk.CTkFrame(app)
frame_memoria.pack(pady=5)

memoria_botoes = [
    ("M+", memoria_mais),
    ("M-", memoria_menos),
    ("MR", memoria_recuperar),
    ("MC", memoria_limpar)
]

for i, (texto, comando) in enumerate(memoria_botoes):

    btn = ctk.CTkButton(
        frame_memoria,
        text=texto,
        width=85,
        height=40,
        command=comando
    )

    btn.grid(
        row=0,
        column=i,
        padx=5,
        pady=5
    )
# INICIAR

app.mainloop()