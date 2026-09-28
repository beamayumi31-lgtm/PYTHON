while True:
    try:
        bissexto = int(input('Digite um ano para verificar se é bissexto: '))
        if bissexto >0:
            break
        else:
            print('Digite um ano válido.')
    except ValueError:
        print('Digite um valor válido.')
ano = bissexto % 400 == 0 or bissexto % 4 == 0 and bissexto % 100 != 0
if ano:
    print(f'O ano {bissexto} é bissexto.')
else:
    print(f'O ano {bissexto} não é bissexto.')
while True:
    try:
        mês = int(input('Digite um mês (1-12): '))
        if mês <= 12 and mês>=1 :
            break
        else:
            print('Tente novamente, coloque um mês válido.')
    except ValueError:
            print('Digite um valor válido.')

if mês in ([3 or 5 or 7 or 8 or 10 or 12]):
    print('Possuem 31 dias.')

elif mês in ([4 or 6 or 9 or 11]):
    print('Possuem 30 dias')

elif mês == 2 and ano:
    print('Possuem 29 dias')

else:
    print('Possuem 28 dias')



