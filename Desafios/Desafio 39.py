# Leitor de ano # 
from datetime import date

ano = int(input('Coloque o ano em que você nasceu: '))
data = date.today().year
idade = data - ano
menor = (idade - 18) * -1
maior = (18 - idade) * -1

if idade < 18:
    print(f'Você ainda não precisa se alistar faltam {menor} ano(s).')
elif idade == 18:
    print(f'Você precisa se alistar pois já tem {idade} anos de idade!!!')
else:
    print(f'Você já se alistou a {maior} ano(s) atrás !!!')