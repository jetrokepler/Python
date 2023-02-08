# ESTRUTURA SEQUENCIAL

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = 3.14
area = float

unidade = input("Informe a unidade de medida (KM / M / CM): ")

if  unidade != "km" and unidade != "KM" and unidade != "Quilômetros" and unidade != "m" and unidade != "M" and unidade != "Metros" and unidade != "cm" and unidade != "CM" and unidade !=  "Centímetros":

    unidade = input("Erro! \n Informe a unidade de medida válida (KM / M / CM): ")

raio = float(input("Informe o valor do raio do círculo: "))

area = pi * raio * raio

if unidade == "km" or unidade == "KM" or unidade == "Quilômetros" or unidade == "QUILÔMETROS":
    
    print(f"O valor da área do círculo é de{area: .2f}km.")

elif unidade == "m" or unidade == "M" or unidade == "Metros" or unidade == "QUILÔMETROS":

    print(f"O valor da área do círculo é de{area: .2f}m.")

elif unidade == "cm" or unidade == "CM" or unidade == "Centímetros" or unidade == "CENTÍMETROS":

    print(f"O valor da área do círculo é de{area: .2f}cm.")