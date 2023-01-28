preco = float(input('Qual o preço do produto? R$'))
condicao = int(input(
    '''Forma de pagamento: 
    [ 1 ] à vista 
    [ 2 ] à vista no cartão 
    [ 3 ] 2x no cartão 
    [ 4 ] 3x ou mais no cartão
Escolha a opção: '''))

if condicao == 1:
    desconto = preco - (preco * 10/100)
    print(f'Com desconto de 10% você irá pagar R${desconto:.2f} a vista!')
elif condicao == 2:
    desconto = preco - (preco * 5/100)
    print(f'Com desconto de 5% você irá pagar R${desconto:.2f}!')
elif condicao == 3:
    print(f'Sua compra será 2x de R${preco/2:.2f}!')
elif condicao == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = (preco + (preco * 20/100)) / parcela
    print(f'Você irá pagar 10x de R${juros:.2f} com juros!')
else:
    print('Opção inválida. Tente Novamente!')
    
