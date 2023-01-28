from random import choice

while True:
    jogador = input('Pedra, Papel ou Tesoura? ').lower()
    maquina = choice(['pedra', 'papel', 'tesoura'])

    if jogador == 'pedra' and maquina == 'papel':
        print('Você escolheu pedra, a máquina escolheu papel, ela ganhou!')
    elif jogador == 'papel' and maquina == 'tesoura':
        print('Você escolheu papel, a máquina escolheu tesoura, ela ganhou!')
    elif jogador == 'tesoura' and maquina == 'pedra':
        print('Você escolheu tesoura, a máquina escolheu pedra, ela ganhou!')
    elif jogador == 'tesoura' and maquina == 'papel':
        print('Você escolheu tesoura, a máquina escolheu papel, você ganhou!')
    elif jogador == 'pedra' and maquina == 'tesoura':
        print('Você escolheu pedra, a máquina escolheu tesoura, você ganhou!')
    elif jogador == 'papel' and maquina == 'pedra':
        print('Você escolheu papel, a máquina escolheu pedra, você ganhou!')
    else:
        print(
            f'Você escolheu {jogador} e a máquina escolheu {maquina}, empate!')
