n = int(input('Digite um número: '))
print(
    '''Escolha: 
    [ 1 ] converter para BINÁRIO 
    [ 2 ] converter para OCTAL 
    [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'A conversão de {n} para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'A conversão de {n} para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'A conversão de {n} para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
