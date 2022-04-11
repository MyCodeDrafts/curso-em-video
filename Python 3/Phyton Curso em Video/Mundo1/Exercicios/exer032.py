#  Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input("Digite um ano pra saber se ele é Bissexto, para calcular o ano atual digite 0: "))
if ano == 0:
    ano = date.today().year
bis = ano % 4 == 0, ano % 400 == 0, ano % 100 == 0

if ano == bis:
    print('Você escolheu o ano {} é \033[1;31mBissexto\033[m'.format(ano))
else:
    print('Você escolheu o ano {} \033[4;7;43mNÃO\033[m é \033[1;31mBISSEXTO '.format(ano))


#  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Forma do professor
