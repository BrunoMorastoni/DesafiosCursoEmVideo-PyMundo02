# Criando um Menu de Opções #
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

menu = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n---> Qual é a sua opção? '))
while menu in [1,2,3,4,5]:
    if menu == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    if menu == 2:
        print(f'A multiplicação entre {n1} X {n2} é {n1*n2}')
    if menu == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = 'Os valores são iguais'
        print(f'O maior número entre {n1} e {n2} é {maior}')
    if menu == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    if menu == 5:
        print('Finalizando...')
        break
    else:
        menu = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n---> Qual é a sua opção? '))
else:
    print('Verificar resultados, opção inválida!!!')