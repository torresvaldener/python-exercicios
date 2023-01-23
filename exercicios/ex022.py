nome = str(input('Digite seu nome completo: '))
print(
    f'Nome => {nome} \nMaiusculo => {nome.upper()} \nMinusculo => {nome.lower()} \nTamanho total => {len(nome.replace(" ", ""))} letras \nPrimeiro nome => {len(nome.split()[0])} letras')
