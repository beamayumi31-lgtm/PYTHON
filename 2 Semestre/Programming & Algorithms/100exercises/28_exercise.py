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
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Os valores digitados podem formar um triângulo.')
else:
    print('Os valores digitados não podem formar um triângulo.')
    
