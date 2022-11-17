# Análise de dados do grupo #

# vars
dezo = ho = mu = 0


while True:
    print('='*50)
    print('Cadastre uma Pessoa'.center(50))
    print('='*50)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M|F] ')).upper()
    print('='*50)
    cont = str(input('Quer continuar? [S|N] ')).upper()
    
    # condições
    if idade >= 18:
        dezo += 1
    if sexo == 'M':
        ho += 1
    if sexo == 'F' and idade < 20:
        mu += 1

    if cont == 'N':
        print('='*50)
        print(f'O total de pessoas com mais de 18 anos foi: {dezo}'.center(50))
        print(f'Ao todo temos {ho} homens cadastrados.'.center(50))
        print(f'Temos {mu} mulheres com menos de 20 anos.'.center(50))
        print('='*50)
        break
