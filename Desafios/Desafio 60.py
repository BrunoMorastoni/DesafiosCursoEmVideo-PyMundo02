# Cálculo do Fatorial #
from math import factorial

n = int(input('Digite um número para calcular o fatorial: '))
r = factorial(n)
f = n

while f > 0:
    print(f'{f}', end= '')
    print(' X ' if f > 1 else ' = ', end= '')
    f -= 1
print(f'{r}')