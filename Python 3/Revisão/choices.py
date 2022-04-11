from random import randint
from time import sleep

ex = randint(5, 55)
print('\033[1;4;35mO exercício que será resolvido é o\033[m \033[1;31m>>>>\033[m  ', end='')
sleep(2)
print('\033[1;34m{}'.format(ex))
