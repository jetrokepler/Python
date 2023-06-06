# Questão 16 - Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.

idade: int
somaidade: int
contagem: int
mediaidades: float

idade = 1
somaidade = 0
contagem = 0
mediaidades = 0.0

while idade != 0:
    
    idade = int(input("Informe sua idade: "))

    somaidade += idade
    contagem += 1

mediaidades = somaidade / (contagem - 1)

print("Média das idade digitadas: ", mediaidades)