#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pinta-lo, sabendo que cada litro de tinta pinta uma área de 2m²
# -*- coding: utf-8 -*
largura_da_parede = float(input('Qual a largura da parede: '))
altura_da_parede = float(input('Qual a altura da parede: '))
área = largura_da_parede * altura_da_parede
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura_da_parede, altura_da_parede, área))
print('Para pintar essa parede, você precisará de {}l tinta'.format(área / 2))

