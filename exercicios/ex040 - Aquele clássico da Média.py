n1 = float(input('Qual foi a sua nota? '))
n2 = float(input('Qual foi a sua nota? '))
media = (n1+n2)/2

if media >= 7:
    print(
        f'Suas notas foram {n1} e {n2}. Tendo como resultado a média {media}. \nAPROVADO!')
elif 6.9 >= media > 5:
    print(
        f'Suas notas foram {n1} e {n2}. Tendo como resultado a media {media}. \nRECUPERAÇÃO!')
else:
    print(
        f'Suas notas foram {n1} e {n2}. Tendo como resultado a media {media}. \nREPROVADO!')
