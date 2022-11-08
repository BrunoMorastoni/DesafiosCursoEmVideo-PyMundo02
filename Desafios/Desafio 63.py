# Sequência de Fibonacci v1.0 #
t = int(input('Quantos termos você quer mostrar? '))

n1 = 0
n2 = 1
c = 0

if t <= 0:
    print('Favor digitar um número maior que zero.')
elif t == 1:
    print(n1)
else:
    while c < t:
        print(n1, end='')
        print(' - ' if c <= t else 'Fim', end='')
        conta = n1 + n2
        n1 = n2
        n2 = conta
        c += 1
    print('Fim')