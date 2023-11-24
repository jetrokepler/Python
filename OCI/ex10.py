# Aprovado ou Reprovado

a, b = map(float, input().split())

if (a + b) / 2 >= 7:
    print("Aprovado")
elif (a + b) / 2 < 7 and (a + b) / 2 >= 4:
    print("Recuperacao")
else:
    print("reprovado")