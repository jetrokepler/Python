# Questão 04 - Faça um programa que receba um número, calcule e mostre a tabuada desse número.

num: int
numero: int

numero = int(input("Informe um número: "))

for num in range(0, 11):
    
    print(f"{numero} x {num} = {numero * num}")