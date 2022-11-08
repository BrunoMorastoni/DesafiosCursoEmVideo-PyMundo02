# Maior e Menor valores #
soma = media = q = maior = menor = 0
resposta = 'S'

while resposta in 'S':
    numeros = int(input('Digite um número: '))
    q += 1
    soma += numeros
    if q == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    resposta = str(input('Quer continuar? [S|N] ')).upper()[0]

media = soma / q
print(f'Você digitou {q} números e a média foi de {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
