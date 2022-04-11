#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo (Divisível por 1 e por ele mesmo)

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end='')
    print(' {}'.format(c), end=' ')
print('\033[m\nO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
