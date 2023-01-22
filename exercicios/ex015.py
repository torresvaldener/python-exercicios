# Aluguel de Carros
km = float(input('Quantos KM o carro percorreu? '))
dia = int(input('Por quantos dias o carro foi alugado? '))
soma = (dia * 60) + (km * 0.15)
print(f'Com {km}Km percorridos e {dia} dias alugados, o valor total será de R${soma}')
