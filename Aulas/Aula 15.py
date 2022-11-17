cont = 1
while True:
    print(f'{cont}', end=' ')
    cont += 1
print('Acabou')

# Com gambiarra
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print(f'A soma vale {s - 999}')

# Usando método certo com um break no meio
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
