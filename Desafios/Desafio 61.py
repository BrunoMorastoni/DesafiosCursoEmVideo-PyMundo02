# Progressão Aritmética v2.0 #
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dt = t
c = 1

while c <= 10:
    print(f'{dt} - ', end='')
    dt += r
    c += 1
print(' Fim!!!')