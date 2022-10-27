# Contagem regressiva #
from time import sleep
print('Os fogos vão estourar em...')

for c in range(0, 10):
    t = ((c + 9) - 19) * (-1)
    print(t)
    sleep(1)
print('BUM')