n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'Os números são {n1} e {n2}.')
if n1 > n2:
    print('O primeiro valor é maior!')
elif n1 == n2:
    print('Os valores são iguais!')
else:
    print('O segundo valor é maior!')
