while True:
    try:
        peso = float(input('Digite o peso em kilogramas:'))
        if peso>0 : 
            break
        else: 
            print('Peso inválido, digite um valor positivo.')
    except ValueError:
        print('Peso inválido, digite um valor numérico.')
while True:
    try: 
        altura = float(input('Digite a altura em metros:'))
        if altura>0 and altura<3: 
            break
        else: 
            print('Altura inválida, digite um valor positivo.')
    except ValueError:
        print('Altura inválida, digite um valor numérico.')
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'IMC = {IMC}. Assim, Classificação: Abaixo da faixa')
elif IMC >= 18.5 and IMC < 25:
    print(f'IMC = {IMC}. Assim, Classificação: Faixa normal')
elif IMC >= 25 and IMC < 30:
    print(f'IMC = {IMC}. Assim, Classificação: Acima da faixa')
else:
    print(f'IMC = {IMC}. Assim, Classificação: Faixa elevada')
