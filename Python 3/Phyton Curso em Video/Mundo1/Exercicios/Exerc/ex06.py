#  CRIE UM ALGORITMO QUE UM LEIA NÚMERO E MOSTRA O SEU DOBRO, O TRIPLO E RAIZ QUADRADA

from math import sqrt
print('\033[1;4;30;43mPara saber o dobro a raiz, o triplo e a raiz quadrada de um número\033[m')
n = int(input('\033[1;32mDigite um número aqui : \033[m'))
print('O dobro de {} é \033[1;31m{}\033[m'.format(n, n * 2))
print('O triplo de {} é \033[1;31m{}\033[m'.format(n, n * 3))
print('A raiz quadrada de {} é \033[1;31m{:.0f}\033[m'.format(n, sqrt(n)))
