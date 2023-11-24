# Prêmio do Milhão

n = int(input())

num_dias = 0
a = 0

for i in range(0, n):
    a += int(input())
    num_dias += 1

    if a >= 1000000:
        print(num_dias) 
        break