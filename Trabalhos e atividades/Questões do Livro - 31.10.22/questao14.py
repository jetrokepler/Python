# Questão 14 - Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme: ótimo — 3; bom — 2; regular — 1. Faça um programa que receba a idade e a opinião de quinze espectadores, calcule e mostre:

# A média das idades das pessoas que responderam ótimo;
# A quantidade de pessoas que responderam regular; e
# A percentagem de pessoas que responderam bom, entre todos os espectadores analisados.

import os

idade: int
opiniao: int
regular: int
bom: int
otimo: int
mio: float
sio: float
porbom: float

otimo = 0
bom = 0
idade = 0
opiniao = 0
mio = 0
sio = 0
regular = 0

for n in range(1, 16):
    
    idade = int(input("Informe sua idade: "))
    opiniao = int(input("\nÓtimo — 3\nBom — 2\nRegular — 1\nInforme sua opinião:"))

    os.system("cls")

    sio += idade

    if opiniao == 3:
        otimo += 1
        sio += idade
    if opiniao == 1:
        regular += 1
    if opiniao == 2:
        bom += 1

mio = sio / otimo
porbom = bom / 15 * 100

print("Média de idades de pessoas que responderam ótimo: ", mio)
print("Quantidade de pessoas que responderam: ", regular)
print("Percentagem de pessoas que responderam bom: ", porbom)