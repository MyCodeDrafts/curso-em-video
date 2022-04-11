# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL,
# MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
# -*- coding: utf-8 -*-
termo = int(input('Digite o 1º termo da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(0, 10):
    pa = termo + (10 - 1) * razão

print('Os 10 primeiros termos são: {}'.format(c), end='')
