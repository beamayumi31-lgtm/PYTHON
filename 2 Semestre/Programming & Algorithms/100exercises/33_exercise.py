while True:
    try:
        numero = int(input('Digite um número: '))
        print('As opções são: 1 - segunda-feira, 2 - terça-feira, 3 - quarta-feira, 4 - quinta-feira, 5 - sexta-feira, 6 - sábado, 7 - domingo')
        if numero >= 1 and numero <= 7:
            opção = {
                1: 'segunda-feira',
                2: 'terça-feira',
                3: 'quarta-feira',
                4: 'quinta-feira',
                5: 'sexta-feira',
                6: 'sábado',
                7: 'domingo'
            }
            print(f'O número {numero} corresponde ao dia da semana: {opção[numero]}')
            break
        else:
            print(f'O número {numero} não está dentro do intervalo de 1 a 7.')
            break
    except ValueError:
        print('Por favor, digite um número válido.')
