# Números primos #
ni = int(input('Digite um número inteiro: '))
for c in range (1, ni + 1):
    if ni % c == 0:
        print(f'{c} é primo',)
    else:
        print(f'{c} não é primo',)
