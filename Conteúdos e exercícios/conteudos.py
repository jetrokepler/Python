#Capítulo I
#Conceitos básicos.

# ALGORÍTIMO

# Um algoritmo é um conjunto de etapas utilizadas para resolver problemas de forma organizada. É uma sequência finita de comandos, uma sequeência lógica de procedimentos.

# Um algoritmo possui três etapas:
# Entrada - É a etapa que obtém as informações de entrada para o algoritmo, ou seja, as informações que ele vai processar;
# Processamento - Faz o trabalho do algoritmo, ou seja, faz o que tem que fazer;
# Saída - Mostra o resultado do algoritmo.

# Exemplo - Algoritmo de uma média aritmética:
# Entrada - 3,7,9,2;
# Processamento - 3 + 7 + 9 + 2 / 4
# Saída - 5,25

# E na programação, como funciona?
# Na programação, utilizamos as linguagens de programação para criar algoritmos, ou seja, utilizamos as linguagens para escrever comandos que explicam ao computador, passo a passo, etapa por etapa, o que ele deve fazer. Explica-se quais e como as entradas serão obtidas, como ele deve processar essas entradas, e como ele deve exibir a saída.

# ENTRADA E SAÍDA

from array import array


input() # O input é utilizado para entrada de dados, para receber alguma informação digitada pelo usuário.

print("Olá, seja bem vindo!") # O print é utilizado para saída de dados, para imprimir algo na tela.

user = input("Informe seu nome: ")
print("olá," + user + "Como vai?")

# VARIÁVEIS

# Por quê usar vairáveis?
# O motivo principal de usar variáveis, em qualquer linguagem de programação, é porque elas são uma forma de você ter um lugar para guardar os dados recebidos do seu programa, como suas expressões, cálculos, em um lugar, para que possa ser reutilizado de outra forma, em outro momento. 

velocidademax = 240 # Esse tipo de variável é chamado int, pois apresenta um número inteiro.

# Para ver essa informação na tela, usa-se o comando print:

print(velocidademax)

frase = "Olá, seja bem vindo!" # Esse tipo de variável é chamado String (str) pois é um local onde posso guardar caracteres, frases, textos, símbolos especiais, e, de forma geral, tudo que é colocado dentro das aspas, serão interpretadas como texto.

print(frase)

# Em algumas situações será necessário tomar decisões dentro do seu programa, e para tomar decisões será necessário entender se algo é vedadeiro ou falso. True é usado para verdadeiro e False para falso, esses valores são chamados de boleanos (bool).

possuicpf = True
possuicnh = False

# Também exisite um tipo de variável que armazena valores decimais, essas variáveis são chamadas de float.

dolaramericano = 5.34

# existe também, um jeito de descobrir o tipo de uma variável:

print(type(velocidademax))
print(type(frase))
print(type(possuicpf))
print(type(possuicnh))
print(type(dolaramericano))

# Também dá para colocar atribuir valores à mais de uma variável em uma mesma linha:

velocidade,frase,possuicpf,dolaramericano = 240,"Olá, seja bem vindo!",True,5.34

# Esse é o primeiro pilar da programação, o pilar das variáveis.

# OPERADOR DE ATRIBUIÇÃO (=)

# Um operador de atribuição tem como objetivo colocar um valor dentro de uma variável. A depender da posição direita ou esquerda de uma variável em relação ao operador de atribuição, ela pode desepenhar um papel ativo ou passivo.

primeirovalor = 50 # A variável está colocada à esquerda, de tal forma que ela desempenha um papel passivo, ou seja, ela será modificada pelo o que está do lado direito.

segundovalor = primeirovalor # Neste caso, a variável está colocada à direita, desempenhando um papel ativo, ou seja, modificando o que está do lado esquerdo.

#OPERADORES ARITMÉTICOS (+,-,*,/,%)

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

# Exemplo dois - Algoritmo utilizando operadores aritméticos - Valor de desconto.

valor = float
desconto = float
valorcomdesconto = float

valor = float(input("Informe o valor do produto: "))
desconto = int(input("Informe o valor do desconto (em %): "))
valorcomdesconto = desconto / 100 * valor

print("O valor com desconto é igual a: " + str(valorcomdesconto))

# DECLARAÇÕES CONDICIONAIS

# O uso das declarações condicionais permite que o algoritmo possa optar entre fazer uma coisa ou outra, com base no que nós conhecemos como expressão condicional.

# if
# O comando if é uma edeclaração condicional, e o comando é executado caso a expressão condicional seja verdadeira.

idade = int
if idade < 18:
    print("Você não pode acesssar o sistema!") # O camando if pode restornar dois possiveis valores, verdadeiro e falso. O comando será executado apenas se a expressão condicional retornar o valor verdadeiro.

# else
# O comando else complementa o sentido do comando if. O else, cria aquilo que chamamos de fluxo alternativo, com o objetivo de definir a ação que será executada se a expressão condicional retornar um valor falso.

if idade < 18:
    print("Você não pode acesssar o sistema!")
else:
    print("Bem vindo ao sistema!") # O que irá acontecer no caso do if retornar um valor falso será a execução do else, em vez da execução do if.

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
    print("Aprovado! O resultado é: " + str(mediaponderada))
else:
    print("Reprovado! O resultado é: " + str(mediaponderada))

# ESTRUTURAS CONDICIONAIS

# As estruturas condicionais são declarações condicionais aninhadas, dclarações condicionais colocadas uma dentro da outra.

if idade < 12:
    print("Categoria: INFANTIL")
else:
    if idade < 16:
        print("Categoria: JUVENIL")
    else:
        if idade < 20:
            print("Categoria: JÚNIOR")
        else:
            print("Categoria: ADULTO")

# As estruturas condicionais, de uma forma padrão, sofrem de um grave problema: a falta de legibilidade, fazendo com que o algoritmo cresça para a direita, com uma forma triangular e deixando as coisas embaralhadas. Foi pra isso que surgiu o elif (else if). Funciona assim: ao invés de utilizarmos um if dentro de um else, trocamos por elif.

if idade < 12:
    print("Categoria: INFANTIL")
elif idade < 16:
    print("Categoria: JUVENIL")
elif idade < 20:
    print("Categoria: JÚNIOR")
else:
    print("Categoria: ADULTO")

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

print("Salário: " + salario)
print("Alíquota: " + str(aliquota) + "%")
print("Imposto mensal:" + str(impostomensal))
print("Imposto anual:" + str(impostoanual))

# OPERADORES RELACIONAIS (>,<,>=,<=,==,!)

# Os operadores relacionais representam a terceira categoria de operadores da programação, e são usados para comparar valores de variáveis e criar expressões condicionais.

# > representa maior que;
# < representa menor que;
# >= representa maior ou igual;
# <= representa menor ou igual;
# == representa igual;
# != representa diferente.

# Eles são usados nas declarações condicionais, as estruturas if e else.

# OPERADORES LÓGICOS (&&,||,!)

# Os operadores lógicos são utilizados em programação para criar expressões condicionais masi complexas.

# && ou and representa conjunção lógica;
# || ou or representa disjunção lógica;
# !  ou not representa negação lógica.

# Esses operadores são usados com o intuito de criar expressões  do tipo verdadeiro ou falso, mas o seu funcionamento é um pouco mais complexo de compreender. Esses operadores geralmente são utilizados junto com os operadores relacionais.

# && ou and.

nivelacesso = 12
if idade > 18 and nivelacesso > 10:
    print("Você pode acessar o sistema!") # O operador lógico && junta as duas expressões em uma única expressão maior, fazendo com que o if só seja executado caso as duas expressões sejam verdadeiras. O operador lógico junta duas ou mais expressões em uma só, com o objetivo montar uma expressão maior e mais complexa. Com a conjunção lógica, uma das expressões pode até ser verdadadeira, mas se uma for falsa, toda a expressão se torma falsa.

# || ou or.
# A disjunção lógica funciona de maneira bem parecida com o operador &&, a diferença, é na regra de avaliação.

idade = 16
nivelacesso = 12
if idade > 18 or nivelacesso > 10:
    print("Você pode acessar o sistema!") # A expressão idade retornará um valor falso, já a expressão nivelacesso retornará um valor verdadeiro, dessa forma, pelo fato que uma das duas é verdadeira, a expressão como um todo se torna verdadeira. Para o operador de disjunção lógica, basta apenas que uma das expressões seja verdadeira.

# ! ou not.
# O operador de negação lógica, funciona com um inversor do resultado lógico.

idade = 16
if idade > 18:
    print("Você pode acessar o sistema!") # Observe que a expressão idade retorna falso, e como resultado, o comando não será executado. Porém podemos usar o operador de negação lógica para inverter o resultado da expressão assim:

idade = 16
if  not (idade > 18):
    print("Você pode acessar o sistema!")

# OPERADORES COMPOSTOS (++, --)

# Os operadores compostos fornecem uma maneira mais curta para realizar algumas operações aritméticas. Os dois algoritmos abaixa mostram o mesmo resultado, de forma diferente.

x = 10
x = x + 15
print (x)

x = 10
x += 5
print (x)

# ++ representa incremento;
# -- representa decremento;
# += representa atribuição-adição;
# -= representa atribuição-subtração;
# *= representa atribuição-multiplicação;
# /= representa atribuição-divisão;
# %= representa atribuição-resto.

x = x - 5 # x -= 5;
x = x * 8 # x *= 8.

# Exemplo - Valor com desconto, desconto de 12%.

valor = float(input("Digite o valor do produto: "))

valor -= (valor * 12/100) # valor = valor - (valor *12/100)

print("Valor com desconto: ", valor)

# ESTRUTURAS DE REPETIÇÃO

# Também conhecida como loop ou laço, uma estrutura de repetição é uma construção que as lingugens de programação fornecem para que o programador possa economizar trabalho e esforço na escrita de um código. Imagine que precisamos escrever um algoritmo para imprimir uma mensagem na tela 10 vezes.

print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")
print("Mensagem")

# Esse código imprime a mensagem na tela dez vezes, mas ele tem um problema de baixa escalabilidade, na sua capacidade de crescimento. Para resover esse tipo de problema, surgiram as estrutras de repetição.

# While.
# É uma estrutura de controle que repete um bloco de comandos enquanto uma condição for verdadeira.

# Exemplo - Programa que obriga o usuário a sempre digitar um valor positivo, e qunaod o valor for positivo, exibir o número na tela.

numero = int(input("Escreva um número inteiro (mairo que 0): "))

while numero < 0:
    numero = int(input("Número inválido. Insira um novo número inteiro maior que zero: "))

print("Número digitado: " + str (numero))

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

# 1 - Comando break.
# O comando break, assim como o comando continue, também interrompe de forma antecipada, porém, ele interrompe toda a estrutura. Ao invés de pular para a próxima repetição, ele simplesmente abandona toda a estrutura de repetição.

number = 0

for number in range(10):
    if number == 5:
        break

    print("O número é: " + str(number))

print("Acabou o loop.")


# 2 - Comando continue.
# O comando continue é um comando auxiliar, e ele força a estrutura a pular para a próxima repetição. A instrução continue lhe dá a opção de pular a parte de um loop onde uma condição externa é acionada, mas continuar para completar o resto do loop.

number = 0

for number in range(10):
    if number == 5:
        continue

    print("O número é:" + str(number))

print("Acabou o loop.")

# Aqui, "O número é 5" nunca ocorre na saída, mas o loop continua depois desse ponto para imprimir linhas para os números de 6 a 10 antes de sair do loop.

# SWITCH CASE

# O comando switch case é uma ferramenta utilizada para construir estruturas condicionais de forma mais elegante. Ele fornece um mecanismo para substituir as estruturas que usam if e else aninhados por uma estrutura mais limpa e objetiva.

# Exemplo - Calculadora simples.

sinal = input("Escolha uma operação (+, -, *, /): ")

while sinal != "+" and sinal != "-" and sinal != "*" and sinal != "/":
    sinal = input("Sinal inválido! Escolha um operador (+, -, *, /): ")

operando1 = float(input("Informe o primeiro operando: "))
operando2 = float(input("Informe o segundo operando: "))

if sinal == "/" and operando2 == 0:
    operando2 = float(input("Operação inválida. Digite o operando 2, agora diferente de zero: "))

# O switch case não tem suportre no Python 3, por isso utiliza-se operadores condicionais.

if sinal == "+":
    resultado = operando1 + operando2
if sinal == "-":
    resultado = operando1 - operando2
if sinal == "*":
    resultado = operando1 * operando2
if sinal == "/":
    resultado = operando1 / operando2

print(str(operando1) + " " + sinal + " " + str(operando2) + " " + "=" + " " + str(resultado))