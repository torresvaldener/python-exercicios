n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'Os números são {n1} e {n2}. O PRIMEIRO valor é maior!')
elif n2 > n1:
    print(f'Os números são {n1} e {n2}. O SEGUNDO valor é maior!')
else:
    print(f'Os números são {n1} e {n2}. Os valores são IGUAIS!')
