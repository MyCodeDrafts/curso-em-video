#  Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

número1 = int(input('Primeiro valor: '))
número2 = int(input('Segundo valor: '))
número3 = int(input('Terceiro valor: '))
#  Verificando o menor
menor = número1
if número2 < número1 and número2 < número3:
    menor = número2
if número3 < número1 and número3 < número2:
    menor = número3

# Verificando o maior
maior = número1
if número2 > número1 and número2 > número3:
    maior = número2
if número3 > número1 and número3 > número2:
    maior = número3
print('O Menor valor digitado foi: \033[1;4;31m{}\033[m'.format(menor))
print('O Maior valor digitado foi: \033[1;31;4m{}\033[m'.format(maior))
