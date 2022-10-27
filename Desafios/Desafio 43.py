# Índice de Massa Corporal #
print('Vamos calcular seu IMC')
peso = float(input('Qual o seu peso em (Kg)? '))
altura = float(input('Qual a sua altura em (m)? '))
imc = peso / (altura ** 2)

if imc != 0:
    print(f'Seu IMC é {imc:.1f}, vamos verificar...')
    if imc < 18.5:
        print(f'Você está abaixo do peso.')
    elif imc >= 18.5 and imc <= 25:
        print(f'Você está no peso ideal.')
    elif imc > 25 and imc <= 30:
        print(f'Você está com sobrepeso.')
    elif imc > 30 and imc <= 40:
        print(f'Você está com obesiade.')
    else:
        print(f'Você está com obesidade mórbida.')
else:
    print('Favor verificar respostas!!!')