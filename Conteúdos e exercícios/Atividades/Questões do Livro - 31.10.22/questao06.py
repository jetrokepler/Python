# Questão 06 - Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:

# O valor total das compras à vista;
# O valor total das compras a prazo;
# O valor total das compras efetuadas; e
# O valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes.

import os

transacao: str
compra: float
avista: float
aprazo: float

compra = 0
avista = 0
aprazo = 0
transacao = ""

for num in range(1, 16):

    print(f"Informações da venda nº{num}:")

    while (transacao != "V" and transacao != "P"):
        transacao = input(
            "Digite o código da compra (V - à vista ou P - a prazo): ").upper()
        if transacao == "V":
            compra = float(input("Digite o valor da compra: R$ "))
            avista = avista + compra
        elif transacao == "P":
            compra = float(input("Digite o valor da compra: R$ "))
            aprazo = aprazo + compra
    transacao = ""

    os.system("cls")

print(f"O valor total à vista: R$ {avista:.2f}")
print(f"O valor total a prazo: R$ {aprazo:.2f}")
print(f"O valor total das compras: R$ {aprazo + avista:.2f}")
print(f"O valor da primeira prestação das compras a prazo juntas (devisão em três vezes): R$ {aprazo/3:.2f}")