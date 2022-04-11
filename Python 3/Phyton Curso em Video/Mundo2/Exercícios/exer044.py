#  Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# à vista dinheiro ou cheque: 10% desconto
# à vista no cartão: 5% de desconto
# em até 2 vezes no cartão: preço normal
# 3x ou mais no cartão 20% de juros
#  print('{:=40}'.format(' LOJA DO PROGRAMADOR '))
print('\033[1;30m==\033[m' * 5, "\033[4;1;34mJOHNNY'S STORE\033[m", '\033[1;30m==\033[m' * 5)
preço = float(input('Preço das compras: R$ '))
pgto = int(input('''Formas de pagamento
[ 1 ] À vista dinheiro/cheque 10% DESCONTO
[ 2 ] À vista Cartão 5% DESCONTO
[ 3 ] 2x no Cartão PREÇO NORMAL
[ 4 ] 3x ou mais no Cartão 20% JUROS
Qual opção desejada: '''))
if pgto == 1:
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(preço, preço - (preço * 10 / 100)))
elif pgto == 2:
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(preço, preço - (preço * 5 / 100)))
elif pgto == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preço / 2))
    print('Sua compra de {:.2f} vai custar R$ {:.2f} no final'.format(preço, preço))
elif pgto == 4:
    parc = int(input('Quantas parcelas? '))
    print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS\nSua compra de R$ {:.2f} vai custar R${:.2f} no final.'''
          .format(parc, (preço + (preço * 20 / 100)) / parc, preço, preço + (preço * 20 / 100)))
else:
    print('\033[1;4;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!!')
