# Super Progressão Aritmética v3.0 #
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
t = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{t} - ', end='')
        t += razao
        c += 1
    print('<=>')
    mais = int(input('Quantos termos a mais você quer na razão? '))

print(f'Progressão finalizada com {total} termos.')