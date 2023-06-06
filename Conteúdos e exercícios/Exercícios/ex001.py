# OPERADORES ARITMÉTICOS (+,-,*,/,%)

# As principais liguagens de programação utilizam os operadores aritméticos para realizar as operações básicas dá Matemática.

# + representa soma;
# - representa subtração;
# * representa multiplicação;
# / representa divisão;
# ** representa exponenciação;
# % representa resto da divisão.

# Exemplo um - Algoritmo ulitilizando operadores aritméticos - Média aritmética.

# Declaração de variáveis.
nota1 = int
nota2 = int
nota3 = int
nota4 = int
media = float

# Entrada de dados.
nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))
nota4 = int(input("Informe a quarta nota: "))

# Processamento.
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída de dados.
print("O resultado é: " + str(media))