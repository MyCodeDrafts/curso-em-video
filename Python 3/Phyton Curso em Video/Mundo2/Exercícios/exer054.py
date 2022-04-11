#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
#  atingiram a maioridade e quantas já são maiores. (21 anos)

from datetime import date

cont = 0
for d in range(1, 8):
    data = int(input('Em que ano a {}ª nasceu? '.format(d)))
if date.today().year - data >= 21:
    cont += 1
    print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
else:
    print('O total de pessoas que não são maiores de 21 anos é de {}')
