# Questão 05 - Faça um programa que mostre as tabuadas dos números de 1 a 10

num1: int
num2: int

for num1 in range(1, 11):

    for num2 in range(0, 11):

        print(f"{num1} x {num2} = {num2 * num1}")

    print()