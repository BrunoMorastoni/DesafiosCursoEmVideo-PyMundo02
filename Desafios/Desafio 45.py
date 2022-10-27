# GAME: Pedra Papel e Tesoura #
import random
print('Vamos jogar Jokenpô'.center(50,' '))
print('Pedra[0]'.center(50,'-'))
print('Papel[1]'.center(50,'-'))
print('Tesoura[2]'.center(50,'-'))
j = int(input('Selecione uma opção: '))
b = random.randint(0,2)
op = ('Pedra', 'Papel', 'Tesoura')

if (j == 0 and b == 0) or (j == 1 and b == 1) or (j == 2 and b == 2):
    print(f'Empate! o oponente jogou {op[b]}')
elif (j == 0 and b == 1) or (j == 1 and b == 2) or (j == 2 and b == 0):
    print(f'Perdeu! o oponente jogou {op[b]}')
elif (j == 0 and b == 2) or (j == 1 and b == 0) or (j == 2 and b == 1):
    print(f'Ganhou! o oponente jogou {op[b]}')
else:
    print('Favor verificar resposta!')