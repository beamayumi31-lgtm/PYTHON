while True:
    try:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        if nota1 < 0 or nota1 >10 or nota2<0 or nota2>10:
            print('Notas inválidas. Digite novamente.')
        else:
            break
    except ValueError:
        print('Entrada inválida. Digite um número válido.')

media = (nota1 + nota2) / 2
print(f'Média: {media}')

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
    
