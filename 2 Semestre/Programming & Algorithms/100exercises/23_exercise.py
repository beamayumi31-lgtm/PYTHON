while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if idade < 16: 
    print('Você não pode votar ainda.')
elif idade>=16 and idade<=17 or idade>=70:
    print('Você pode votar opcionalmente.')
else:
    print('O seu voto é obrigatório.')
