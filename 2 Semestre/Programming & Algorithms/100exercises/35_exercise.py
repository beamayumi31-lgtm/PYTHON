while True:
    try:
        idade = int(input('Idade: '))
        if idade>0 and idade<200:
            break
        else:
            print('Tente novamente colocar a idade válida.')
    except ValueError:
        print('Coloque um valor válido')
ingresso = int(30.00)
while True:
    try:
        estudante = input('Você é estudante? ').strip().lower()
        if estudante in ['sim', 'nao', 'não']:
            break
        else:
            print('Opção inválida! Responda apenas com sim ou nao.\n')
    except ValueError:
        print('Coloque um valor válido:')
if estudante in ['sim', 's'] or idade < 12 or idade >= 60:
    valor = ingresso // 2
    print(f'O valor gasto para o ingresso é de R${valor}')
else: 
    print(f'O valor gasto para o ingresso é de R${ingresso}')
