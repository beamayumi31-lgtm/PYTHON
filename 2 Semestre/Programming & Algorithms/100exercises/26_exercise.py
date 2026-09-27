while True: 
    try:
       salario = float (input('Digite o salário atual: R$'))
       if salario > 0: 
           break
       else:
              print('O salário deve ser maior que zero. Tente novamente.')
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido para o salário.')
if salario <= 1500:
    aumento1500 = (salario * 0.15) + salario
    print(f'O salário atual é R${aumento1500}, ou seja, conteve um reajuste de 15%.')
elif salario > 1500.01 and salario <= 3000:
    aumento15001 = (salario * 0.10) + salario
    print(f'O salário atual é R${aumento15001}, ou seja, conteve um reajuste de 10%.')
else:
    aumento3000 = (salario * 0.05) + salario
    print(f'O salário atual é R${aumento3000}, ou seja, conteve um reajuste de 5%.')
