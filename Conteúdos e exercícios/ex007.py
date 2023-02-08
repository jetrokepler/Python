# SWITCH CASE

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
elif sinal == "-":
    resultado = operando1 - operando2
elif sinal == "*":
    resultado = operando1 * operando2
elif sinal == "/":
    resultado = operando1 / operando2

print(str(operando1) + " " + sinal + " " + str(operando2) + " " + "=" + " " + str(resultado))