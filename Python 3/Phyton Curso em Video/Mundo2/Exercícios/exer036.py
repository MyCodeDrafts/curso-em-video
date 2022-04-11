#  Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
#  o Valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
#  sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa R$ '))
salário = float(input('Digite o seu salário atual R$ '))
anos = int(input('Digite em quantos anos vai pagar a casa: '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')