#  Faça um programa que leia número inteiro e mostre na tela o seu sucessor e antecessor

#  n = int(input('Digite um número: '))

#   print('Você digitou {}. O número antecessor é {}, o sucessor é {}'.format(n, (n - 1), (n + 1)))
import time

n = int(input('Olá, digite um número para saber o seu sucessor e antecessor: '))
time.sleep(1)
print('Só um momento...')
time.sleep(2)
print("""'Você digitou o número \033[1;31m{}\033[m, seu antecessor é \033[4;1m{}\033[m e o 
Sucessor é \033[4;1m{}\033[m!'""".format(n, n-1, n-2))
