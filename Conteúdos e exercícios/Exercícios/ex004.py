# ESTRUTURAS CONDICIONAIS

# Exemplo - Cálculo de imposto de renda.

salario = float(input("Digite o salário bruto mensal: R$"))

if salario > 4664.68:
    aliquota = 37.5
    deducao = 869.36
elif salario <= 4664.68 and salario >= 3751.06:
    aliquota = 22.5
    deducao = 636.13
elif salario <= 3751.06 and salario >= 2826.66:
    aliquota = 15
    deducao = 354.80
elif salario <= 2826.66 and salario >= 1903.99:
    aliquota = 7.5
    deducao = 142.80
else:
    aliquota = 0
    deducao = 0
impostomensal = salario * (aliquota / 100) - deducao
impostoanual = impostomensal * 12

print("Salário: " + str(salario))
print("Alíquota: "+ str(aliquota) + "%")
print("Imposto mensal : " + str(impostomensal))
print("Imposto anual : " + str(impostoanual))