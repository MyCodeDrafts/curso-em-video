# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
# EX: Digite um número: 6.127 o número 6.127 tem a parte inteira 6
import math
'''from math import floor

n = float(input('Digite um número: '))
print('O valor digitado foi {}, a sua porção inteira é {}'.format(n, floor(n)))

# Outra maneira é usando 'TRUNC' '''
n = float(input('Digite um número: '))
print('O valor digitado foi {}, e sua porção inteira é: {}'.format(n, int(n)))

