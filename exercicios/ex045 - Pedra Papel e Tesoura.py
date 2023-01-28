from random import choice

while True:
    jogador = input('Pedra, Papel ou Tesoura? ').lower()
    computador = choice(['pedra', 'papel', 'tesoura'])

    if jogador == 'pedra' and computador == 'papel':
        print('Você escolheu pedra, a máquina escolheu papel, ela ganhou!')
    elif jogador == 'papel' and computador == 'tesoura':
        print('Você escolheu papel, a máquina escolheu tesoura, ela ganhou!')
    elif jogador == 'tesoura' and computador == 'pedra':
        print('Você escolheu tesoura, a máquina escolheu pedra, ela ganhou!')
    elif jogador == 'tesoura' and computador == 'papel':
        print('Você escolheu tesoura, a máquina escolheu papel, você ganhou!')
    elif jogador == 'pedra' and computador == 'tesoura':
        print('Você escolheu pedra, a máquina escolheu tesoura, você ganhou!')
    elif jogador == 'papel' and computador == 'pedra':
        print('Você escolheu papel, a máquina escolheu pedra, você ganhou!')
    else:
        print(
            f'Você escolheu {jogador} e a máquina escolheu {computador}, empate!')
