# Questão 10 - Faça um programa que receba dez números, calcule e mostre a soma dos números pares e a soma dos números primos.

import math

num: int
somapares: int
somaprimos: int
contagem: int

contagem = 0
somapares = 0
somaprimos = 0

for n in range(1, 4):

    num = int(input("Digite um número: "))

    if num % 2 == 0:
        somapares += num

    for m in range(1, int(math.sqrt(num)+1)):
        
        if num % m == 0:
            contagem += 1

    if contagem == 0:
        somaprimos += num

print(f"Soma dos números pares: {somapares}")
print(f"Soma dos números primos: {somaprimos}")