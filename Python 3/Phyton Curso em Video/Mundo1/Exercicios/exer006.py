# Crie um algoritmo que leia número e mostre o seu dobro, o triplo e raiz quadrada
import math
t = input('Olá digite seu nome: ')
n = int(input('Agora digite um número: '))
print(t, ', o dobro de {} é: {}. \n O triplo é: {}. \n A raiz quadrada é: {}'.format(n, (n * 2), (n * 3), math.sqrt(n)))



