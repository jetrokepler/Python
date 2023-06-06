# Questão 08 - Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e C — castanho) e a cor dos cabelos (P — preto; C — castanho; l — louro; e R — ruivo) de seis pessoas, e que calcule e mostre:

# A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
# A média das idades das pessoas com altura inferior a 1,50 m;
# A porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
# A quantidade de pessoas ruivas e que não possuem olhos azuis

idade: int
numI50P60: int
somaidade: int
numidade: int
numolhoazul: int
numruivosemazul: int
peso: float
altura: float
peso60: float
corolho: str
corcabelo: str

somaIdade = 0
numidade = 0
numolhoazul = 0
numruivosemazul = 0
numI50P60 = 0

for num in range(1, 7):

    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe o altura: "))

    corolho = input("Informe a cor dos olhos (A — azul; P — preto; V — verde; C — castanho): ")
    corcabelo = input("Informe a cor dos cabelos (P — preto; C — castanho; L — Louro; R — ruivo): ")

    if idade > 50 and peso < 60:
        numI50P60 = + 1
    if altura < 1.50:
        somaIdade += idade
        numidade += 1
    if corolho == "A":
        numolhoazul += 1
    if corcabelo == "R" and corolho != "A":
        numruivosemazul += 1

print(f"Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg: {numI50P60}")
print(f"Média das idades das pessoas com altura inferior a 1,50 m: {somaIdade/numidade}")
print(f"Porcentagem de pessoas com olhos azuis entre todas as pessoas: {numolhoazul/6*100:.2f}%")
print(f"Quantidade de pessoas ruivas e que não possuem olhos azuis: {numruivosemazul}")