n = int(input('Digite um número: '))
un = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10
print(
    f'Unidade => {un} \nDezena => {dez} \nCentena => {cent} \nMilhar => {mil}')
