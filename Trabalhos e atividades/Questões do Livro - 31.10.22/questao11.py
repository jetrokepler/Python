# Questão 11

valorcarro: float
avista: float
juros: float

valorcarro = 0.0
avista = 0.0
juros = 0.03

valorcarro = float(input("Informe o valor do carro: "))

avista = valorcarro - (valorcarro*0.20)

print("Quantidade de parcelas menos porcentagem de juros:")    

for n in range(6, 66, 6):

    print(f"{n} - {valorcarro + valorcarro*juros}")

    juros = juros + 0.03