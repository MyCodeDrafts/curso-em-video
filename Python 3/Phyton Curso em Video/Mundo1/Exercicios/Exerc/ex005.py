# FAÇA UM PROGRAMA QUE LEIA NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E ANTECESSOR
import time
n = int(input('Olá, digite um número para saber o seu sucessor e antecessor: '))
print('\033[1;m-> Só um momento <-\033[m')
time.sleep(2)
print("""'Você digitou o número \033[1;31m{}\033[m, seu antecessor é \033[4;1;43m{}\033[m e o 
Sucessor é \033[4;1;43m{}\033[m!'""".format(n, n-1, n-2))