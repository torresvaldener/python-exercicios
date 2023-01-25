distancia = float(input('Qual a distância em Km da viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da sua passagem será de R${preco:.2f}')

