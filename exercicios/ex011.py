# Área da parede e quantidade de tintas necessárias

n1 = int(input('Quanto de largura tem sua parede? '))
n2 = int(input('Quanto de altura tem sua parede? '))
area = n1 * n2
tintas = area / 2
print(f'Para pintar uma área de {area} metros, é necessário {tintas} litros de tinta')