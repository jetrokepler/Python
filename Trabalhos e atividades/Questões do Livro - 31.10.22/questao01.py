# Questão 01 - Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e mostre-os na ordem lida. Em seguida, organize-os em ordem crescente e decrescente.

valorA: int
valorB: int
ValorC: int
ValorD: int
num: int
primeiro: int
segundo: int
terceiro: int
quarto: int

primeiro = 0
segundo = 0
terceiro = 0
quarto = 0

for num in range(1, 6):
    
    print(f"Informe os valores para o grupo nº{num}: ")
    
    valorA = int(input("Informe o valor de A: "))
    valorB = int(input("Informe o valor de B: "))
    ValorC = int(input("Informe o valor de C: "))
    ValorD = int(input("Informe o valor de D: "))
    
    if valorA > valorB and valorA > ValorC and valorA > ValorD:
        primeiro = valorA
        if valorB > ValorC and valorB > ValorD:
            segundo = valorB
            if ValorC > ValorD:
                terceiro = ValorC
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = ValorC
        elif ValorC > valorB and ValorC > ValorD:
            segundo = ValorC
            if valorB > ValorD:
                terceiro = valorB
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = valorB
        else:
            segundo = ValorD
            if valorB > ValorC:
                terceiro = valorB
                quarto = ValorC
            else:
                terceiro = ValorC
                quarto = valorB
    if valorB > valorA and valorB > ValorC and valorB > ValorD:
        primeiro = valorB
        if valorA > ValorC and valorA > ValorD:
            segundo = valorA
            if ValorC > ValorD:
                terceiro = ValorC
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = ValorC
        elif ValorC > valorA and ValorC > ValorD:
            segundo = ValorC
            if valorA > ValorD:
                terceiro = valorA
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = valorA
        else:
            segundo = ValorD
            if valorA > ValorC:
                terceiro = valorA
                quarto = ValorC
            else:
                terceiro = ValorC
                quarto = valorA
    if ValorC > valorA and ValorC > valorB and ValorC > ValorD:
        primeiro = ValorC
        if valorA > valorB and valorA > ValorD:
            segundo = valorA
            if valorB > ValorD:
                terceiro = valorB
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = valorB
        elif valorB > valorA and valorB > ValorD:
            segundo = valorB
            if valorA > ValorD:
                terceiro = valorA
                quarto = ValorD
            else:
                terceiro = ValorD
                quarto = valorA
        else:
            segundo = ValorD
            if valorA > valorB:
                terceiro = valorA
                quarto = valorB
            else:
                terceiro = valorB
                quarto = valorA
    if ValorD > valorA and ValorD > valorB and ValorD > ValorC:
        primeiro = ValorD
        if valorA > valorB and valorA > ValorC:
            segundo = valorA
            if valorB > ValorC:
                terceiro = valorB
                quarto = ValorC
            else:
                terceiro = ValorC
                quarto = valorB
        elif ValorC > valorB and ValorC > valorA:
            segundo = ValorC
            if valorB > valorA:
                terceiro = valorB
                quarto = valorA
            else:
                terceiro = valorA
                quarto = valorB
        else:
            segundo = valorB
            if valorA > ValorC:
                terceiro = valorA
                quarto = ValorC
            else:
                terceiro = ValorC
                quarto = valorA

    print(f"Valores recebidos: {valorA}, {valorB}, {ValorC} e {ValorD}")
    print(f"Valores recebidos em ordem crescente: {quarto}, {terceiro}, {segundo} e {primeiro}")
    print(f"Valores recebidos em ordem decrescente: {primeiro}, {segundo}, {terceiro} e {quarto}")