# Questão 12 - Faça um programa que receba dez números inteiros e mostre a quantidade de números primos dentre os números que foram digitados.

import math

num: int
contagem: int
numprimos: int

num = 0
contagem = 0
numprimos = 0

for n in range(1, 4):

    num = int(input("Digite número: "))

    for m in range(2, int(math.sqrt(num)+1)):
        
        if num % m == 0:
            contagem += 1

    if contagem == 0:
        numprimos += 1

    contagem = 0

print(f"Quantidade de números primos: {numprimos}")