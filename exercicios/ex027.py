# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip().split()
print(
    f'Muito prazer em te conhecer! \nSeu primeiro nome é {nome[0]} \nSeu último nome é {nome[-1]}')
