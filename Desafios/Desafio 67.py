# Tabuada v3.0 #
n = 0
while True:
    n = int(input(
        'Quer ver a tabuada de qual valor?\n[coloque um número negativo para encerrar]\n'))
    for t in range(1, 11):
        print('=' * 25)
        print((f'{n} X {t} = {n*t}').center(25, ' '))
        print('=' * 25)
    if n < 0:
        print('Tabudada encerrada. Volte sempre!!!')
        break
