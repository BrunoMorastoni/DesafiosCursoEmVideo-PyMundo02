# Tratando vários valores v1.0 #
n = int(input('Digite um número - [999 para parar] '))
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número - [999 para parar] '))
    c += 1
    soma += n
print(f'Você digitou {c} números e a soma entre eles foi {soma - 999}.')