# Gerenciador de Pagamentos #
p = float(input('Qual o valor do produto? R$:'))
dvista = p - (p * 10/100) 
cvista = p - (p * 5/100)
cartao2x = p
cartao3x = p + (p * 20/100)

if p != 0:
    print('Qual será o método de pagamento?')
    print('[1] Dinheiro à vista, com 10% de desconto')
    print('[2] Cartão à vista, com 5% de desconto')
    print('[3] Cartão 2x, sem juros')
    print('[4] Cartão 3x ou mais, com 20% de juros')
    m = int(input(''))
    if m == 1:
        print(f'O valor ficou R$:{dvista:.2f}')
    elif m == 2:
        print(f'O valor ficou R$:{cvista:.2f}')
    elif m == 3:
        print(f'O valor ficou R$:{cartao2x:.2f}')
    elif m == 4:
        print(f'O valor ficou R$:{cartao3x:.2f}')
    else:
        print('Favor verificar resposta!')
else:
    print('Favor verificar resposta!')