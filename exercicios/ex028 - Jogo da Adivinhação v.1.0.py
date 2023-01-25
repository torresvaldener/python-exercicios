from time import sleep
from random import choice
n = int(input('Adivinhe o número de 0 a 5: '))
lista = choice([0, 1, 2, 3, 4, 5])
print('Processando...')
sleep(3)
if n == lista:
    print('Você acertou o número.')
else:
    print(f'Você disse {n}. Errou! Eu pensei no {lista}')
