salario_fixo = float(input('Salário fixo: R$'))
total_vendido = float(input('Total vendido: R$'))
comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao
print('Comissão: R${}'.format(comissao))
print('Salário total: R${}'.format(salario_total))
