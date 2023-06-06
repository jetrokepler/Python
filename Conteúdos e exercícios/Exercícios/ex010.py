# ESTRUTURA SEQUENCIAL

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float

salporhr = float(input("Informe quanto você ganha por hora: "))
numhrmensal = int(input("Informe quantas horas você trabalha por mês: "))

salario = salporhr * numhrmensal

print(f"Seu salário mensal é de{salario: .2f}.")