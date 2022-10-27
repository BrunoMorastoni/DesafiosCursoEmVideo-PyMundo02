# Média de nota #
print('Calculador de média')
nota1 = float(input('Coloque a 1ª nota que você tirou: '))
nota2 = float(input('Coloque a 2 nota que você tirou: '))
media = (nota1 + nota2) / 2
nrec = 2 * (7 - media)

if media <= 5.0:
    print(f'Sua média ficou {media:.2} ')
    print(f'REPROVADO')
elif media >= 7.0:
    print(f'Sua média ficou {media:.2} ')
    print(f'APROVADO')
else:
    print(f'Sua média ficou {media:.2} ')
    print(f'RECUPERAÇÃO, será necessário tirar {nrec}')