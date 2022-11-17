# Estatísticas em produtos #

total = mil = p_preco = contador = 0
p_barato = ' '

print('='*50)
print(f'Loja comum com preços normais'.center(50))
print('='*50)

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont = str(input('Quer continuar? [S|N]')).upper()
    contador += 1

    if preco > 1000:
        mil += 1

    if contador == 1:
        p_preco = preco
        p_barato = produto
    else:
        if preco < p_preco:
            p_preco = preco

    total += preco

    if cont == 'N':
        print(' Fim '.center(50, '='))
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {mil} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {p_barato} que custa {p_preco:.2f}')
        break
