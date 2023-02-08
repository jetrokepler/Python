# Questão 07 - Faça um programa que receba a idade, a altura e o peso de cinco pessoas, calcule e mostre:

# A quantidade de pessoas com idade superior a 50 anos;
# A média das alturas das pessoas com idade entre 10 e 20 anos;
# A porcentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas.

import os

idade: int
maior50anos: int
tamanho10e20: int
inferior40kg: int
numcadastros: int
altura: float
peso: float
somaAltura: float

maior50anos = 0
altura = 0
somaAltura = 0
tamanho10e20 = 0
inferior40kg = 0
numcadastros = 0

os.system("cls")

numcadastros = int(input("Informe o nº de cadastros para realizar: "))

for n in range(1, numcadastros + 1):

    print(f"Informe os dados para {numcadastros} pessoas!")
    print(f"Informe os dados para {n}ª pessoa:")

    idade = int(input("Informe a idade: "))
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))

    os.system("cls")

    if idade > 50:
        maior50anos += 1
    if idade >= 10 and idade <= 20:
        somaAltura += altura
        tamanho10e20 += 1
    if peso < 40:
        inferior40kg += 1

print(f"Existem {maior50anos} pessoas com idade superior a 50 anos.")

if  tamanho10e20 <= 0:

    print("Não foram informadas pessoas com média de alturas entre 10 e 20 anos")

else:

    print(f"A média das alturas entre 10 e 20 anos é de {somaAltura/tamanho10e20:.2f}m")

print(f"% pessoas com peso inferior a 40kg: {inferior40kg/numcadastros*100}%")