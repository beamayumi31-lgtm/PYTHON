while True:
    try:
        valor_imovel = float(input("Digite o valor do imóvel: R$"))
        salario = float(input("Digite o valor do salário: R$"))
        prazo = int(input("Digite o prazo em anos: "))
        if valor_imovel > 0 and salario > 0 and prazo > 0:
            break
        else:
            print("Os valores devem ser maiores que zero. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para os valores.")
prestação = valor_imovel / (prazo * 12)
if prestação > (salario * 0.3):
    print(f"Empréstimo não concedido. A prestação mensal excede 30% do salário.")
    print('Resultado: REPROVADO')
else:
    print(f"Empréstimo concedido. A prestação mensal é de R${prestação}")
    print(f'Limite: R${salario * 0.3}')
    print('Resultado: APROVADO')
