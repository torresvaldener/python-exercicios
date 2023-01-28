valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempoAnual = int(input('Em quantos anos você pretende pagar? '))

prestacaoMensal = valorCasa / (tempoAnual * 12)

print(
    f'Para pagar uma casa de R${valorCasa} em {tempoAnual} anos a prestação será de R${prestacaoMensal:.2f} ao mês!')

if prestacaoMensal > salario * 30/100:
    print('Emprestimo negado')
else:
    print('Emprestimo concedido!')
