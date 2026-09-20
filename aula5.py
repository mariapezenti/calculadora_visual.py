print ("\n==== SISTEMA DE INGRESSOS ====")

continuar = True

total_clientes = 0 
total_ingressos = 0 
meia_entrada = 0 
entrada_inteira = 0
total_arrecadado = 0

while continuar:

    nome = input("Nome do cliente:")
    idade = int(input("Idade:"))
    resposta = input("É Estudante? (sim/não):").lower()
    estudante = resposta == "sim"
    quantidade = int(input("Quantidade de ingressos:"))

    if idade < 12:
        valor_ingresso = 15.00
        tipo = "Meia-Entrada"
        meia_entrada += 1

    elif idade >=60:
        valor_ingresso = 15.00
        tipo = "Meia-Entrada"
        meia_entrada += 1
    elif estudante:
        valor_ingresso = 15.00
        tipo = "Meia-Entrada"
        meia_entrada += 1
    else:
        valor_ingresso = 30.00
        tipo = "Ingresso cheio"
        entrada_inteira += 1
    for numero in range (1,quantidade +1):
        print(f"Ingresso {numero} emitido para {nome}")
    total_compra = valor_ingresso * quantidade

    print (f"Tipo: {tipo}")
    print (f"Valor unitári: R$ {valor_ingresso:.2f}")
    print (f"Quantidade: {quantidade}")
    print (f"Total da compra: R$ {total_compra:.2f}")

    total_clientes += 1
    total_ingressos += quantidade
    total_arrecadado += total_compra

    resposta = input("Deseja cadastrar outro cliente? (sim/não): ").lower()
    continuar = resposta == "sim"

print ("\n==== RESUMO FINAL ====")
print (f"Total de clientes atendidos: {total_clientes}")
print (f"Total de ingressos vendidos: {total_ingressos}")
print (f"Quantidade de clientes com meia-entrada: {meia_entrada}")
print (f"Quantidade de clientes com entrada inteira: {entrada_inteira}")
print (f"Valor total arrecadado: R$ {total_arrecadado:.2f}")