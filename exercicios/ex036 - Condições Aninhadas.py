valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
pagamento = float(input('Em quantos anos você pretende pagar? '))

tempo = valor / pagamento

if salario * 30/100 <= salario:
    print('Emprestimo negado')
else:
    print('Emprestimo aceito!')

print(f'O tempo de pagamento será de {tempo:.2f} anos')

if
