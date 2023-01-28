from datetime import date
anoNascimento = int(input('Ano de nascimento? '))
idade = date.today().year - anoNascimento

if idade <= 9:
    print(f'O Atleta tem {idade} anos. \nCategoria: MIRIM')
elif idade <= 14:
    print(f'O Atleta tem {idade} anos. \nCategoria: INFANTIL')
elif idade <= 19:
    print(f'O Atleta tem {idade} anos. \nCategoria: JUNIOR')
elif idade <= 25:
    print(f'O Atleta tem {idade} anos. \nCategoria: SENIOR')
else:
    print(f'O Atleta tem {idade} anos. \nCategoria: MASTER')
