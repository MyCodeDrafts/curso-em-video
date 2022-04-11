# DESAFIO 036 **********
# ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA
# CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO
# PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

valor_da_casa = float(input('Valor do imóvel R$: '))
salario = float(input('Digite o valor do seu salário R$: '))
anos = float(input('Em quantos anos de financiamento? ')).__ceil__()
valor_parcelas = valor_da_casa / (anos * 12) # Cálcudo da prestação, preço da casa multiplicado por meses
minimo = salario * (30/100)
print('Para comprar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor_da_casa, anos, valor_parcelas))
if valor_parcelas <= minimo:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')