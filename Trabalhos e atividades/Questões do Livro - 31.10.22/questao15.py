# Questão 15 - Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado. Para isso, forneceu o sexo do entrevistado e sua resposta (S — sim; ou N — não). Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:

# o número de pessoas que responderam sim;
# o número de pessoas que responderam não;
# o número de mulheres que responderam sim;
# a percentagem de homens que responderam não, entre todos os homens analisados.

sexo: str
resposta: str
totalsim: int
totalnao: int
msim: int
hnao: int
hsim: int
htotal: int
porh: float

sexo = ""
resposta = ""
totalsim = 0
msim = 0
totalnao = 0
porh = 0
hnao = 0
hsim = 0
htotal = 0

for n in range(1, 11):
    
    sexo = input("Digite seu sexo (F - Feminino ou M - Masculino): ")
    resposta = input("Qual sua resposta? (S — sim; ou N — não)")

    if resposta == "S":
        totalsim += 1
        if sexo == "F":
            msim += 1
        else:
            hsim += 1

    if resposta == "N":
        totalnao += 1
        if sexo == "M":
            hnao += 1

htotal = hnao + hsim
porh = hnao / htotal * 100

print("O número de pessoas que responderam sim: ", totalsim)
print("O número de pessoas que responderam não: ", totalnao)
print("O número de mulheres que responderam sim: ", msim)
print("O percentagem de homens que responderam não, entre homens: ", porh)