# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por diaR$0,15 por Km rodado.
vd = float(input('Qual valor do aluguel diário? R$ '))
vkm = float(input('Qual o valor de km rodado? R$ '))
d = int(input('Quantos dias alugados? '))
kmr = float(input('Quantos KM rodados? '))
total = (kmr * vkm) + d * vd
print('Total a pagar é de R${:.2f}'.format(total))
