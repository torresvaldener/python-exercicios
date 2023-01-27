preco = float(input('Qual o preço do produto? '))
condicao = int(input(
    'Qual será o meio de pagamento? \n1- A vista \n2- A vista no cartão \n3- 2x no cartão \n4- 3x ou mais no cartão \nForma de pagamento: '))

if condicao == 1:
    desconto = preco - (preco * 10/100)
    print(f'Com desconto de 10% você irá pagar R${desconto} a vista!')
elif condicao == 2:
    desconto = preco - (preco * 5/100)
    print(f'Com desconto de 5% você irá pagar R${desconto}!')
elif condicao == 4:
    juros = preco + (preco * 20/100)
    print(f'Com juros de 20% você irá pagar R${juros}!')
else:
    print(f'Em 2x no cartão você irá pagar no total R${preco}!')
