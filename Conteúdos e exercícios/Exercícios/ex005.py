# ESTRUTURAS DE REPETIÇÃO

# While.
# É uma estrutura de controle que repete um bloco de comandos enquanto uma condição for verdadeira.

# Exemplo - Programa que obriga o usuário a sempre digitar um valor positivo, e qunaod o valor for positivo, exibir o número na tela.

numero = int(input("Escreva um número inteiro (mairo que 0): "))

while numero < 0:
    numero = int(input("Número inválido. Insira um novo número inteiro maior que zero: "))

print("Número digitado: " + str (numero))