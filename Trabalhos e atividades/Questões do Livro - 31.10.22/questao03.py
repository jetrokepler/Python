# Questão 03

idade: int
fx1: int
fx2: int
fx3: int
fx4: int
fx5: int

fx1 = 0
fx2 = 0
fx3 = 0
fx4 = 0
fx5 = 0

for num in range(1, 9):
    
    idade = int(input("Informe a idade: "))

    if idade <= 15:
        fx1 = fx1 + 1
    elif idade > 15 and idade <= 30:
        fx2 += 1
    elif idade > 30 and idade <= 45:
        fx3 += 1
    elif idade > 45 and idade <= 60:
        fx4 += 1
    else:
        fx5 += 1

print(f"Faixa etária nº1 (até 15 anos): {fx1}")
print(f"Faixa etária nº2 (16 a 30 anos): {fx2}")
print(f"Faixa etária nº3 (31 a 45 anos): {fx3}")
print(f"Faixa etária nº4 (46 a 60 anos): {fx4}")
print(f"Faixa etária nº5 (acima de 60 anos): {fx5}")
print(f"Porcentagem de pessoas da primeira faixa em relação ao total: {fx1 / 8 * 100}%")
print(f"Porcentagem de pessoas da última faixa em relação ao total: {fx5 / 8 * 100}%")