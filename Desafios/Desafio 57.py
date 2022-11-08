# Validação de Dados #
s = str(input('Qual o seu sexo?\n[M|F]: ')).upper()
while s not in 'MF':
    s = str(input('Dados inválidos, favor verificar resposta.'))
if s == 'M':
    s = 'Masculino'
elif s == 'F':
    s = 'Feminino' 
print(f'Tudo certo, sexo {s} registrado.')