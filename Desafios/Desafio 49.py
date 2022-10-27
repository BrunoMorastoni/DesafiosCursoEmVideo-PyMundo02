# Tabuada 2.0 #
n = int(input('Coloque um valor inteiro que você quer descobrir a tabuada: '))
print('=' * 25)
for c in range(1, 11):
    print((f'{n} X {c} = {n*c}').center(25,' '))
print('=' * 25)