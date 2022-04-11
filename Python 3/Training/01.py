#  DESAFIO 005
# FAÇA UM PROGRAMA QUE LEIA NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E ANTECESSOR
numero_inteiro = int(input('Digite um número inteiro para saber seu sucessor e antecessor: '))
sucessor = numero_inteiro + 1
antecessor = numero_inteiro - 1
print('O sucessor do número {} é {} e o antecessor é {}'.format(numero_inteiro, sucessor, antecessor))