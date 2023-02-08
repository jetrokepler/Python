# Questão 02 - Uma companhia de teatro deseja montar uma série de espetáculos. A direção calcula que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão de R$ 200,00. Diminuindo-se em R$ 0,50 o preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos. Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse preço de R$ 5,00 a R$ 1,0, de R$ 0,50 em R$ 0,50. Escreva, ainda, para cada novo preço de ingresso, o lucro máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.

preçoing: float
despesa: float
lucro: float
quantidadeing: int

preçoing = 5.00
quantidadeing = 120
despesa = 200.00

while preçoing >= 1.00:

    lucro = quantidadeing * preçoing - despesa

    print(f"|Preço: \t(⌐■_■)/\t|R$ {preçoing:.2f}")
    print(f"|Lucro: \t(⌐■_■)/\t|R$ {lucro:.2f} ")
    print(f"|Ingressos vendidos: \t|{quantidadeing}")
    print("===================================")

    preçoing = preçoing - 0.50
    quantidadeing = quantidadeing + 26