print("=" * 50)
print("SISTEMA DE CLASSIFICAÇÃO DE AMOSTRAS")
print("=" * 50)

quantidade_baixa = 0
quantidade_normal = 0
quantidade_alta = 0

for numero in range(1, 6):
    print(f"\nAmostra {numero}")
    codigo = input("Código da amostra: ")
    resultado = float(input("Resultado numérico: "))

    if resultado < 70:
        classificacao = "Resultado baixo"
        quantidade_baixa += 1
    elif resultado <= 100:
        classificacao = "Resultado dentro do intervalo"
        quantidade_normal += 1
    else:
        classificacao = "Resultado alto"
        quantidade_alta += 1

    print("Código:", codigo)
    print("Resultado:", resultado)
    print("Classificação:", classificacao)

print("\nRESUMO")
print("Resultados baixos:", quantidade_baixa)
print("Resultados normais:", quantidade_normal)
print("Resultados altos:", quantidade_alta)
