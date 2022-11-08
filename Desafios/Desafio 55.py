# Maior e menor da sequência #
maior = 0
menor = 0

for p in range (1, 6):
    peso = float(input(f'Qual o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior:.2f}Kg')
print(f'O menor peso foi {menor:.2f}Kg')