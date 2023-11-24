# Lâmpadas

n = int(input())

la = 0
lb = 0
num = 0

for i in range(0, n):
    if num == 1:
        la = not la
    else:
        la, lb = not la, not lb
    num = int(input())

if la == 1:
    print(1)
else:
    print(0)
if lb == 1:
    print(1)
else:
    print(0)