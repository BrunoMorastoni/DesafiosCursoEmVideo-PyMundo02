# Simulador de Caixa Eletrônico #
print('='*50)
print(f' Banco BGM '.center(50, '-'))
print('='*50)

valor = int(input('Qual valor você dejesa sacar? R$:'))
total = valor
ced = 50
total_cedula = 0

while True:
    if total >= ced:
        total -= ced
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} notas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedula = 0
        if total == 0:
            break

print('='*50)
print('Processo finalizado, volte sempre.')
