# Grupo da Maioridade #
from datetime import date
data = date.today().year
maior = 0
menor = 0

for g in range (1, 8):
    ano = int(input(f'Ano em que a {g}ª pessoa nasceu: '))
    idade = data - ano
    if idade >= 21:
       maior += 1
    else:
        menor += 1

print(f'Tem {maior} pessoas de maior idade.')
print(f'Tem {menor} pessoas de menor idade.')