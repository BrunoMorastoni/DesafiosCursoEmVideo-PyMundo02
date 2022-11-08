# Analisador completo #
media = 0
maiorh = 0
velhonome = ''
tmulher = 0

for c in range (1,5):
    nome = str(input(f'Qual é o {c}ª nome: '))
    idade = int(input(f'Qual é a idade da {c}ª pessoa: '))
    sexo = str(input(f'Qual o sexo da {c}ª pessoa?\n[M]Masc - [F]Fem\n---> '))
    media += idade
    
    if c == 1 and sexo == 'Mm':
        maiorh = idade
        velhonome = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        velhonome = nome
    if sexo in 'Ff' and idade < 20:
        tmulher += 1

print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho se chama {velhonome}, ele tem {maiorh} anos.')
print(f'Existem {tmulher} mulheres com menos de 20 anos.')