# comparador de números #
print('Por favor digite dois números')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

if n1 > n2:
    print(f'O número {n1} é maior')
elif n2 > n1:
    print(f'O número {n2} é maior')
else:
    print(f'Os dois números são iguais')