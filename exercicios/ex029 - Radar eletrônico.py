velocidade = float(input('Digite a velocidade em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(
        f'\033[1;31mVocê será multado pois atingiu {velocidade} Km/h, sua multa será de R${multa:.2f}')
else:
    print('\033[1;32mVocê não será multado.\033[m Boa viagem!')
