while True:
    try:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
            print('Situação: Nota inválida')
        else:
            break 
    except ValueError:
        print('Situação: Nota inválida')

media = (nota1 + nota2) / 2
if media >= 6:
    print(f'Média: {media}. Situação:Aprovado')
else:
    print(f'Média: {media}. Situação: Reprovado')

