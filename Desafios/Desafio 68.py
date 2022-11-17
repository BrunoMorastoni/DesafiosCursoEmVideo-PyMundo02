# Jogo do Par ou Ímpar #
import random
print(f'='*25)
print('Vamos jogar Par ou Ímpar'.center(20))
print(f'='*25)
vitorias = 0

while True:
    v = int(input('Digite um valor de 0 a 10: '))
    op = str(input('Par ou Ímpar? [P|I] ')).upper()
    bot = random.randint(0, 10)
    resultado = v + bot
    par_impar = 0
    if resultado % 2 == 0:
        par_impar = 'Par', 'P'
    else:
        par_impar = 'Ímpar', 'I'

    print(
        f'Voce jogou {v} e o computador {bot}, total de {resultado} deu {par_impar[0]}')
    if op == par_impar:
        print(f'='*25)
        print(f'Você VENCEU !!!'.center(25))
        print(f'='*25)
        v += 1
    else:
        print(f'='*25)
        print(f'Você PERDEU !!!'.center(25))
        print(f'='*25)
        print(f'Game Over - Você venceu {vitorias} vezes.')
        break
