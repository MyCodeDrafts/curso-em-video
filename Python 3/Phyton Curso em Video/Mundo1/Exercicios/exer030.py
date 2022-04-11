#  Crie um programa que leia o número inteiro e mostre se ele é par ou impar
from time import sleep
n = int(input('\033[1;31mDigite um número qualquer para saber se é par ou impar: \033[m'))
print('\033[1;46m  \033[m'*20)
print(' '*10, '\033[34;1mDeixa eu pensar .......\033[m')
print('\033[1;46m  \033[m'*20)
sleep(2)
if (n % 2) == 0:
    print('\033[1;36mEsse número é \033[m \033[31;4mPAR!!')
else:
    print('\033[1;36mEsse número é \033[m \033[31;4mIMPAR!!')