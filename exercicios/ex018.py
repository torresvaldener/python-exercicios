# Seno, Cosseno e Tangente de um ângulo
from math import sin, cos, tan, radians
n = int(input('Digite o ângulo: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
print(f'Angulo de {n}º \nSeno => {seno:.2f} \nCosseno => {cosseno:.2f} \nTangente => {tangente:.2f}!')