while True:
    try:
        numero = float(input('Digite um número: '))
        if numero >= 10 and numero <= 20:
            print(f'O número {numero} é positivo e esta dentro do intervalo.')
            break
        else:
            print(f'O número {numero} não está dentro do intervalo de 10 a 20.')
            break
    except ValueError:
        print('Por favor, digite um número válido.')
