# Aprovação de empréstimo #
vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário atual? '))
qanos =  int(input('Em quantos anos você pretende pagar a casa? '))
prestação = vcasa / (qanos * 12)
tporc = salario * 30/100

print(f'Com o seu salário atual sendo R$:{salario} as parecelas em {qanos} serão de R$:{prestação:.2f}')

if prestação <= tporc:
    print('Parabéns você recebeu o empréstimo')
else :
    print('Você está inapto a receber o empréstimo')