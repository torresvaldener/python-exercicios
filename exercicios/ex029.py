velocidade = int(input('Digite a velocidade em Km/h: '))
limite = 80
if velocidade > 80:
    multa = (velocidade - limite) * 7.00
    print(
        f'Você será multado pois atingiu {velocidade} Km/h, sua multa será de R${multa}')
else:
    print('Você não será multado. Boa viagem!')
