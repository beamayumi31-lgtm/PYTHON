while True: 
    try:
        preço = float(input("Digite o preço do produto: R$"))
        if preço > 0:
            break
        else:
            print("O preço deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para o preço.")
while True:
    try: 
        opcoes = int(input('Veja as opções e digite o número da opção que deseja: 1 - Dinheiro ou Pix, 2 - Débito, 3 - Crédito à vista, 4 - Crédito parcelado: '))
        if opcoes in [1, 2, 3, 4]:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a opção.")
opcao1 = preço - (preço * 0.1)
opcao2 = preço - (preço * 0.05)
opcao3 = preço
opcao4 = preço + (preço * 0.08)

if opcoes == 1: 
    print(f'O valor a ser pago é R${opcao1}. Assim, você terá um desconto de 10% no pagamento à vista em dinheiro ou Pix.')
elif opcoes == 2:
    print(f'O valor a ser pago é R${opcao2}. Assim, você terá um desconto de 5% no pagamento à vista no cartão de débito.')
elif opcoes == 3:
    print(f'O valor a ser pago é R${opcao3}. Assim, você não terá desconto no pagamento à vista no cartão de crédito.')
elif opcoes == 4:
    print(f'O valor a ser pago é R${opcao4}. Assim, você terá um acréscimo de 8% no pagamento parcelado no cartão de crédito.')
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

    
