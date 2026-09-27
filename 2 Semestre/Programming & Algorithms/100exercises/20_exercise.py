numeros = [int(x) for x in input('Digite os números que deseja deixar em ordem crescente: ').split()] 
numeros_crescente = sorted(numeros)
print(f'Os números em ordem crescente são: {numeros_crescente}')
