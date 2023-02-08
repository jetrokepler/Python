# Questão 09 - Faça um programa que receba dez idades, pesos e alturas, calcule e mostre:

# A média das idades das dez pessoas;
# A quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro;
# A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m.

import os

idade: int
somaidade: int
nump90a150: int
numi10e30a190: int
peso: float
altura: float
mediaidade: float

nump90a150 = 0
somaidade = 0
numi10e30a190 = 0

for n in range(0, 10):

    print(f"Dados para {n+1}ª pessoa:")
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))

    os.system("cls")

    somaidade = somaidade + idade

    if (peso > 90) and (altura < 1.50):
        nump90a150 += 1
    if (idade >= 10 and idade <= 30) and altura > 1.90:
        numi10e30a190 += 1

mediaidade = somaidade / 10

print(f"Média das idades das dez pessoas: {mediaidade:.2f}")
print(f"Quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro: {nump90a150}m.")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m: {numi10e30a190/10*100:.1f}%.")