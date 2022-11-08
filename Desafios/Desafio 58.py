# Jogo da Adivinhação v2.0 #
import random

n = int(input('Tente acertar o número, ele está entre 0 e 10\n---> '))
na = random.randint(0, 10)
t = 1
while n != na:
    if n > na:
        n = int(input('ERROU, tente menos\nNúmero: '))
    elif n < na:
        n = int(input('ERROU, tente mais\nNúmero: '))
    
    t += 1

print(f'Parabéns você acertou o número {na}, foram necessárias {t} tentativas!!!')