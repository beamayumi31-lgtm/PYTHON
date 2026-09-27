while True:
    try:
        numero1 = int(input('Digite o primeiro número:'))
        numero2 = int(input('Digite o segundo número:'))
        numero3 = int(input('Digite o terceiro número:'))
        break
    except ValueError:
        print('Por favor, digite apenas números inteiros.') 

print(f'Os valores são {numero1}, {numero2} e {numero3}.')

if numero1> numero2 and numero1>numero3 or numero1==numero2>numero3 or numero1==numero3>numero2:
    print(f'O maior número é {numero1}.')   
elif numero2>numero1 and numero2>numero3 or numero2==numero1>numero3 or numero2==numero3>numero1:
    print(f'O maior número é {numero2}.')
elif numero3>numero1 and numero3>numero2 or numero3==numero1>numero2 or numero3==numero2>numero1:
    print(f'O maior número é {numero3}.')
else:
    print(f'Todos os números são iguais a {numero1}.')   

if numero1< numero2 and numero1<numero3 or numero1==numero2<numero3 or numero1==numero3<numero2:
    print(f'O menor número é {numero1}. ')
elif numero2<numero1 and numero2<numero3 or numero2==numero1<numero3 or numero2==numero3<numero1:
    print(f'O menor número é {numero2}.')
elif numero3<numero1 and numero3<numero2 or numero3==numero1<numero2 or numero3==numero2<numero1:
    print(f'O menor número é {numero3}.')
else :
    print(f'Existem números iguais, portanto não há menor ou maior número.')
