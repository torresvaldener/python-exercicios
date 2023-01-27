from datetime import date
anoNascimento = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - anoNascimento

if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é JUNIOR')
elif idade <= 20:
    print(f'Você tem {idade} anos e sua categoria é SENIOR')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER')
