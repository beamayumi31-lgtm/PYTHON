while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        if numero > 0:
            print(f'O número {numero} é positivo.')
            break
        elif numero < 0:
            print(f'O número {numero} é negativo.')
            break
        else:
            print('O número é zero.')
    except ValueError:
        print('Por favor, digite um número inteiro válido.')
if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 3 e 5.')
elif numero % 3 == 0:
    print(f'O número {numero} é múltiplo de 3.')   
elif numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 5.')
else:
    print(f'O número {numero} não é múltiplo de 3 nem de 5.')
