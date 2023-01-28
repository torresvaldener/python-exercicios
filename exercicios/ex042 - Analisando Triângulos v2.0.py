r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite um comprimento: '))
r3 = float(input('Digite um comprimento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os comprimentos acima formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os comprimentos acima não formam um triângulo')
