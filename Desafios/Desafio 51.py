# Progressão Aritmética #
t = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
dt = t + (10 - 1) * r

for c in range (t, dt + r, r):
    print(c, end=' ')