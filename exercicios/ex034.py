# Aumentos múltiplos
salario = float(input('Qual o seu salário? '))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)

print(
    f'Salário anterior R${salario:.2f} com o aumento será de R${aumento:.2f}!')
