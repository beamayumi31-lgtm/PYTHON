numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
if numero1 > numero2:
    print(f'O maior valor é o primeiro valor: {numero1}')
elif numero1 < numero2:
    print(f'O maior número é o segundo valor: {numero2}')
else: 
    print(f'O primeiro valor é igual ao segundo valor, sendo igual o valor: {numero1}')
