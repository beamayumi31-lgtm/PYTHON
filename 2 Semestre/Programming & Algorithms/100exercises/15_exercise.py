valor_unitario = float(input('Valor unitário: R$'))
quantidade = int(input('Quantidade: '))
frete = float(input('Frete: R$ '))
subtotal = valor_unitario * quantidade
total = subtotal + frete
print('Subtotal: R${}'.format(subtotal))
print('Total: R${}'.format(total))
