while True:
    try:
        bissexto = int(input('Digite um ano para verificar se é bissexto: '))
        if bissexto >0:
            break
        else:
            print('Digite um ano válido.')
    except ValueError:
        print('Digite um valor válido.')

if bissexto % 400 == 0 or bissexto % 4 == 0 and bissexto % 100 != 0:
    print(f'O ano {bissexto} é bissexto.')
else:
    print(f'O ano {bissexto} não é bissexto.')


