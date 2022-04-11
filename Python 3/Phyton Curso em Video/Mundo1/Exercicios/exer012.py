#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
valor = float(input('Digite o valor do produto: R$ '))
vd = valor - (valor * 5/100)
print('O valor do produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(valor, vd))

