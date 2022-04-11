# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente de ângulo.

import math
ang = int(input('Digite o ângulo: '))
s = (math.sin(math.radians(ang)))
c = (math.cos(math.radians(ang)))
t = (math.tan(math.radians(ang)))
print('O ângulo de {} tem\n SENO de {:.2f}\n COSSENO de {:.2f}\n TANGENTE de {:.2f}'.format(ang, s, c, t))
