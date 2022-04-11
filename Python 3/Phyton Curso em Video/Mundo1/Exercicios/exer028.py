# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu

import random
import time



print('\033[31;1;4m-=-\033[0m' * 20)
print('Vou pensar e um número entre 0 e 5. Tente adivinhar ...')
print('\033[31;1;4m-=-\033[0m' * 20)
time.sleep(2)
lista = [0, 1, 2, 3, 4, 5]
n = int(input('Em que número eu pensei? '))
num = random.choice(lista)
print('PROCESSANDO . . . ')
time.sleep(3)
if n != num:
    print('GANHEI. Eu pensei no número {}'.format(num))
else:
    print('PARABÉNS! Você conseguiu me vencer!')


# Resolução igual da aula
#  from random import randint

# computador = randint(0, 5)  # Faz o computador sortear
# print('Pensei no número {}'.format(computador))
# jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
# if jogador == computador:
#    print('PARABÉNS! Você conseguiu me vencer!')
# else:
# print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
