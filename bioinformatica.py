print("===== ANÁLISE SIMPLES DE DNA =====")

sequencia = input("Digite uma sequência de DNA: ").upper()
total_bases = len(sequencia)

quantidade_g = sequencia.count("G")
quantidade_c = sequencia.count("C")
quantidade_a = sequencia.count("A")
quantidade_t = sequencia.count("T")
sequencia_valida = True

for base in sequencia:
    if base not in "ATCG":
        sequencia_valida = False

print("\n=== RESULTADO ===")

print("Sequência:", sequencia)
print("Quantidade de base:", total_bases)
print("Quantidade de A:", quantidade_a)
print("Quantidade de T:", quantidade_t)
print("Quantidade de G:", quantidade_g)
print("Quantidade de C:", quantidade_c)

if sequencia_valida:

    gc = quantidade_g + quantidade_c
    porcentagem_gc = (gc / total_bases) * 100
    print(f"Conteúdo GC: {porcentagem_gc:.2f}%")
    if porcentagem_gc < 40:
        print("Classificação: baixo conteúdo GC")
    elif porcentagem_gc <= 60:
        print("Classificação: conteúdo GC moderado")
    else:
        print("Classificação: alto conteúdo GC")
    print("Sequência válida!")

    complementar = sequencia.replace("A", "1")
    complementar = complementar.replace("T", "A")
    complementar = complementar.replace("1", "T")
    complementar = complementar.replace("C", "2")
    complementar = complementar.replace("G", "C")
    complementar = complementar.replace("2", "G")

    print("\n===ANÁLISE GENÉTICA===")
    print("DNA complementar:", complementar)
    rna = sequencia.replace("T", "U")
    print("RNA:", rna)
    base_original = input("Digite a base que deseja substituir: ").upper()
    nova_base = input("Digite a nova base: ").upper()
    sequencia_mutada = sequencia.replace(base_original, nova_base)

    print("\n===SIMULAÇÃO DE MUTAÇÃO===")
    print("Sequência original:", sequencia)
    print("Sequência mutada:", sequencia_mutada)

    if sequencia == sequencia_mutada:
        print("Não houve mutação.")
    else:
        print("Houve alteração na sequência.")
else:
    print("Sequência inválida!")