# OPERADORES ARITMÉTICOS (+,-,*,/,%)

# As principais liguagens de programação utilizam os operadores aritméticos para realizar as operações básicas dá Matemática.

# + representa soma;
# - representa subtração;
# * representa multiplicação;
# / representa divisão;
# ** representa exponenciação;
# % representa resto da divisão.

# Exemplo dois - Algoritmo utilizando operadores aritméticos - Valor de desconto.

valor = float
desconto = float
valorcomdesconto = float

valor = float(input("Informe o valor do produto: "))
desconto = int(input("Informe o valor do desconto (em %): "))
valorcomdesconto = desconto / 100 * valor

print("O valor com desconto é igual a: " + str(valorcomdesconto))