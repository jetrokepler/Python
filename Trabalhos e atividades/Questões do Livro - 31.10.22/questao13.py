# Questão 13 - Faça um programa que receba a idade e o peso de quinze pessoas, e que calcule e mostre as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e de 31 anos para cima.

idade: int
peso: float

mpf1a10: float
mpf11a20: float
mpf21a30: float
mpf31a: float

spf1a10: float
spf11a20: float
spf21a30: float
spf31a: float

npf1a10: float
npf11a20: float
npf21a30: float
npf31a: float

mpf1a10 = 0
mpf11a20 = 0
mpf21a30 = 0
mpf31a = 0

spf1a10 = 0
spf11a20 = 0
spf21a30 = 0
spf31a = 0

npf1a10 = 0
npf11a20 = 0
npf21a30 = 0
npf31a = 0

for num in range(1, 16):

    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))

    if idade >= 1 and idade <= 10:
        spf1a10 += peso
        npf1a10 += 1

    if idade >= 11 and idade <= 20:
        spf11a20 += peso
        npf11a20 += 1

    if idade >= 21 and idade <= 30:
        spf21a30 += peso
        npf21a30 += 1

    if idade >= 31:
        spf31a += peso
        npf31a += 1

if npf1a10 > 0:
    mpf1a10 = spf1a10 / npf1a10

    print("Média faixa 1 a 10 anos: ", mpf1a10)

else:

    print("Não houve idade na faixa etária entre 1 a 10 anos!")

if npf11a20 > 0:
    mpf11a20 = spf11a20 / npf11a20

    print("Média faixa 11 a 20 anos: ", mpf11a20)

else:

    print("Não houve idade na faixa etária entre 11 a 20 anos!")

if npf21a30 > 0:
    mpf21a30 = spf21a30 / npf21a30

    print("Média faixa 21 a 30 anos: ", mpf21a30)

else:

    print("Não houve idade na faixa etária entre 21 a 30 anos!")

if npf31a > 0:
    mpf31a = spf31a / npf31a

    print("Média faixa 31 anos acima: ", mpf31a)
    
else:
    print("Não houve idade na faixa acima de 31 anos!")