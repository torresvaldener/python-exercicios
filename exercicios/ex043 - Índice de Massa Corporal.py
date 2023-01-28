peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, Abaixo do peso')
elif 18.5 < imc < 25:
    print(f'Seu IMC é de {imc:.1f}, Peso normal')
elif 25 < imc < 30:
    print(f'Seu IMC é de {imc:.1f}, Sobrepeso')
elif 30 < imc < 40:
    print(f'Seu IMC é de {imc:.1f}, Obesidade')
elif imc > 40:
    print(f'Seu IMC é de {imc:.1f}, Obesidade mórbida')
