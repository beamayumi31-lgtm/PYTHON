nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2
if media >= 6:
    print(f'Média: {media}. Situação:Aprovado')
elif media < 0 or media >10:
    print('Situação: Nota inválida')
else:
    print(f'Média: {media}. Situação: Reprovado')
