r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite um comprimento: '))
r3 = float(input('Digite um comprimento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os comprimentos acima formam um triângulo')
else:
    print('Os comprimentos acima não formam um triângulo')

if r1 == r2 == r3:
    print('Triângulo Equilátero: todos os lados iguais')
elif r1 == r2 or r1 == r3 or r3 == r2:
    print('Triângulo Isósceles: dois lados iguais')
else:
    print('Triângulo Escaleno: todos os lados diferentes')
