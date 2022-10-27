# Conversão de número com escolhas #
n = int(input('Coloque um número inteiro: '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)

print('[1] converter para BINÁRIO;')
print('[2] converter para OCTAL;')
print('[3] converter para HEXADECIMAL;')
resp = int(input('Selecione uma opção: '))

if resp == 1:
    print(f'O número {n} em binário é: {binario[2:]}')
elif resp == 2:
    print(f'O número {n} em octário é: {octal[2:]}')
elif resp == 3:
    print(f'O número {n} em hexadecimal é: {hexadecimal[2:]}')
else:
    print('Por favor selecione uma dessas opções [1] [2] [3]')