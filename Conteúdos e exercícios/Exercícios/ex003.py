# DECLARAÇÕES CONDICIONAIS

# Exemplo - Algoritmo utilizando estruturas condicionais - Aprovação e reprovação de um aluno.

nota1 = float
nota2 = float
trabalho = float
mediaponderada = float

nota1 = float(input("Informe a nota da 1º prova (peso de 30%): "))
nota2 = float(input("Informe a nota da 2º prova (peso de 50%): "))
trabalho = float(input("Informe a nota do trabalho (peso de 20%): "))

mediaponderada = ((nota1 * 30) + (nota2 * 50) + (trabalho * 20)) / 100

if mediaponderada >= 7:
    print("Aprovado! O resultado é: " + str (mediaponderada))
else:
    print("Reprovado! O resultado é: " + str(mediaponderada))