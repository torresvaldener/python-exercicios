from datetime import date
anoNascimento = int(input('Qual o seu ano de nascimento? '))
alistamento = int(input('Você já se alistou? \n[1]SIM e [2]NÃO: '))
idade = date.today().year - anoNascimento

if alistamento == 2 and idade == 18:
    print('Esse ano você completa 18 anos, está na hora de se alistar!')
elif alistamento == 2 and idade <= 17:
    faltante = 18 - (idade)
    print(f'Você ainda não precisa se alistar, falta {faltante} ano(s)!')
elif alistamento == 1 and idade <= 17:
    print(f'Não é possível, você ainda é menor de idade.')
elif alistamento == 1:
    print(
        f'Você tem {idade} anos e você já se alistou.')
else:
    print(
        f'Você tem {idade} anos e já passou {(idade) - 18} anos do prazo.')
