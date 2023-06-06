# Questão 03

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
peso1 = float(input("Informe o primeiro peso: "))
peso2 = float(input("Informe o segundo peso: "))
peso3 = float(input("Informe o terceiro peso: "))

calculo1 = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
calculo2 = peso1 + peso2 + peso3
calculo3 = calculo1 / calculo2

print("Resultado da operação: {:.2f}".format(calculo3))