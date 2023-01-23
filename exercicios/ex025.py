# Procurando uma string dentro de outra
nome = str(input('Digite o seu nome: ')).strip()
condicao = 'SILVA' in nome.upper()
print(f'Seu nome tem Silva? {condicao}')
