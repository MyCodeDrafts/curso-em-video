# # -*- coding: utf-8 -*-
# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# - QUANTAS VEZES APARECE A LETRA 'A'
# - EM QUE POSIÇÃO APARECE A PRIMEIRA VEZ
# - EM QUE POSIÇÃO APARECE A ÚLTIMA VEZ

frase = str(input('Digite uma frase qualquer: ')).upper().rstrip().lstrip().strip()
print('Aparece {} a letra "A"'.format(frase.count('A')))
print('A primeira letra "A" aparece na {}ª posição'.format(frase.find('A') + 1))
print('A última letra "A" aparece na {}ª posição'.format(frase.rfind('A') + 1))  # RFIND começa a partir da direita
