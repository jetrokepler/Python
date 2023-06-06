# ESTRUTURAS DE REPETIÇÃO

# For.
# A estrutura de repetição for nada mais é do que uma estrutra de repetição while com algumas modificações. Ele é uma evolução do comando while. O uso dele é indicado quando já se sabe precisamente a quantidade de repetições. A extrutura do comando for é composta por três elementos: inicialização, expressão condicional e iteração (ou incremento).

# Exemplo - Algoritmo de cálculo da média aritmética de um conjunto de notas de um aluno.

numnotas = int (input("Digite a quantidade de notas: "))
media = 0.0 # Variável com valor decimal.

for i in range(numnotas):
    nota = float(input("Digite a nota " + str(i+1) + ": "))
    media = media + nota

media = media / numnotas

print("Média: " + str(media))