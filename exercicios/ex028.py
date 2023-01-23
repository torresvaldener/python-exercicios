from random import choice
n = int(input('Adivinhe o número de 0 a 5: '))
lista = choice([0, 1])

if n == lista:
    print('Você acertou o número')
else:
    print('Você errou o número')
print(lista)
