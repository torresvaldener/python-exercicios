n1 = float(input('Qual foi a sua nota? '))
n2 = float(input('Qual foi a sua nota? '))

if (n1+n2)/2 >= 7:
    print('APROVADO')
elif 6.9 >= (n1+n2)/2 > 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
