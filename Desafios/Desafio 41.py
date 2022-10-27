# Classificando Atletas #
print('Classificação de Natação')
idade = int(input('Quantos anos você tem? '))

if idade <= 9:
    print(f'Você tem {idade} anos --- MIRIM')
elif idade <=14:
    print(f'Você tem {idade} anos --- INFANTIL')
elif idade <=19:
    print(f'Você tem {idade} anos --- JUNIOR')
elif idade <=20:
    print(f'Você tem {idade} anos --- SÊNIOR')
else:
    print(f'Você tem {idade} anos --- MASTER')