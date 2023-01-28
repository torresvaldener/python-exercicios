from datetime import date
anoNascimento = int(input('Qual o seu ano de nascimento? '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade == 18:
    print(f'''Em {anoAtual} você tem {idade} anos. 
Está na hora de se alistar.''')
elif idade < 18:
    faltante = 18 - (idade)
    print(
        f'''Em {anoAtual} você tem {idade} anos. 
        Faltam {faltante} ano para seu alistamento. 
        Será em {anoNascimento + 18}.''')
elif idade > 18:
    print(
        f'''Em {anoAtual} você tem {idade} anos.
Você já deveria ter se alistado há {idade - 18} anos. 
Seu alistamento foi em {anoNascimento + 18}.''')
