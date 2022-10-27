# Analisando Triângulos v2.0 #
r1=float(input('Digite um valor da reta: '))
r2=float(input('Digite um segundo valor da reta: '))
r3=float(input('Digite um ultimo valor da reta: '))
print('Vamos conferir se esses valores formam um triângulo...')
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é um EQUILÁTERO.')
    elif (r1 == r2) or (r1 == r3) or (r2 == r1) or (r2 == r3) or (r3 == r1) or (r3 == r2):
        print('O triângulo é um ISÓSCELES.')
    elif r1 != r2 != r3 and r1 != r3:
        print('O triângulo é ESCALENO.')
else:
    print('Não pode formar um triângulo.')