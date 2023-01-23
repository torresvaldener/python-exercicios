distancia = float(input('Qual a distância em Km da viagem? '))
limite = 200
if distancia <= 200:
    gasto = distancia * 0.50
    print(f'O preço da sua passagem será de {gasto}')
else:
    gasto = distancia * 0.45
    print(f'O preço da sua passagem será de {gasto}')
