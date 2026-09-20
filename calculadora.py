import numpy as np
import sympy as sp
from scipy import special

mem = {"valor": 0.0}
x = sp.Symbol("x")

def ler_numeros(msg= "Digite os números separados por espaço:"):
    return np.array(input(msg).split(), dtype=float)

def ler_dois():
    return ler_numeros("Digite dois números:").tolist()

def soma():
    print("Soma:", np.sum(ler_numeros()))

def multiplicacao():
    print("Multiplicação:", np.prod(ler_numeros()))

def divisao():
    a, b = ler_dois()
    if b == 0:
        print("Erro: divisão por zero.")
    else:
        print("Divisão:", a / b)

def raiz_quadrada():
         print("Raiz Quadrada:", np.emath.sqrt(float(input("Número:"))))

def trigonometria ():
        ang = np.radians(float(input("Angulo em graus:")))
        print(f"Seno: {np.sin(ang):.4f} | Cosseno: {np.cos(ang):.4f} | Tangente: {np.tan(ang):.4f}")
def raiz_cubica():  
        print("Raiz cúbica:", np.cbrt(float(input("Número: "))))
def logaritmo():     
        print("ln:", np.emath.log(float(input("Número: "))))
def fatorial():   
        print("Fatorial:", special.factorial(int(input("n: ")), exact=True))
def mdc():        
        print("MDC:", np.gcd.reduce(ler_numeros().astype(int)))
def media_desvio(): 
        d = ler_numeros(); print("Média:", np.mean(d), "| Desvio:", np.std(d))
def derivada(): 
        print("f'(x) =", sp.diff(sp.sympify(input("f(x) = ")), x))
def integral(): 
        print("Integral =", sp.integrate(sp.sympify(input("f(x) = ")), x))
def equacao():
        print("Raízes:", sp.solve(sp.sympify(input("Equação = 0: ")), x))

def porcentagem():
    total = float(input("Total: "))
    parte = float(input("Parte: "))
    if total == 0:
        print("Erro: total não pode ser zero.")
    else:
        print(f"Porcentagem: {(parte / total) * 100:.2f}%")

acoes_memoria = {
        "a": lambda: mem.update(valor=mem["valor"] + float(input("Valor:"))), #M+
        "b": lambda: mem.update(valor=mem["valor"] - float(input("Valor:"))), #M-
        "c": lambda: mem.update(valor=mem["valor"] * float(input("Valor:"))), #M*
        "d": lambda: mem.update(valor=mem["valor"] / float(input("Valor:"))), #M/
        "e": lambda: mem.update(valor=0)  #MC
    }

def memoria():
    sub = input("a) M+ | b) M- | c) M* | d) M/ | e) MC\nEscolha uma opção: ").lower()
    acoes_memoria.get(sub, lambda: print("Opção inválida."))()

def opcao_invalida():
    print("Opção inválida. Tente novamente.")

operacoes = {
    "1": soma,
    "2": multiplicacao,
    "3": divisao,
    "4": raiz_quadrada,
    "5": trigonometria,
    "6": raiz_cubica,
    "7": logaritmo,
    "8": fatorial,
    "9": mdc,
    "10": media_desvio,
    "11": derivada,
    "12": integral,
    "13": equacao,
    "14": porcentagem,
    "15": memoria
}

while True:
    print("\n === CALCULADORA ===")
    for chave, funcao in operacoes.items():
        print(f"{chave}. {funcao.__name__}")
        print("0.Sair")

    opcao = input("Escolha uma operação: ")
    if opcao == "0":
        print("Saindo da calculadora.")
        break
    try:
        operacoes.get(opcao, opcao_invalida)()
    except Exception as erro:
        print(f"Erro: {erro}")