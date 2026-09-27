while True:
    try:
        lado1 = int(input('Digite o valor do primeiro lado: '))
        lado2 = int(input('Digite o valor do segundo lado: '))
        lado3 = int(input('Digite o valor do terceiro lado: '))
        if lado1 > 0 and lado2 > 0 and lado3 > 0:
            break
        else:
            print('Os valores dos lados devem ser positivos. Tente novamente.')
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')
if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
