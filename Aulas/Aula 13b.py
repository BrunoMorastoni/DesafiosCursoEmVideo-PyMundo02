from tkinter import N


i = int(input('Digite um início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for c in range (i, f+1, p):
    print (c)
print ('Fim')

# Somatório #
s = 0
for c in range (0, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma de todos os valores é {s}')