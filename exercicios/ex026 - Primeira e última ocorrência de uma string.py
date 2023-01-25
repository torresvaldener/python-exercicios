frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase\nA primeira letra A aparece na posição {frase.find("A")+1} \nA última letra A aparece na posição {frase.rfind("A")+1}')
