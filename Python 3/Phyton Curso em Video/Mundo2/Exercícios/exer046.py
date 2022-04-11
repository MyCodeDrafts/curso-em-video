#  Faça um programa que mostre na tela a Contagem regressiva para o estouro de fogos de artifício,
#  indo de 10 até 0, com uma pausa de 1 segundo
import pygame
from time import sleep

n = int(input('''\033[1;42mPara ativar a contagem regressiva para estouro dos rojões\033[m 
 [\033[31;1m 0\033[m ] \033[1;31mSAIR\033[m
 [\033[1;34m 1\033[m ] \033[1;34mCONTAGEM REGRESSIVA\033[m
 Sua opção: '''))
if n == 1:
    print('\033[1;4;34mPREPARE - SE\033[m')
    for c in range(10, -1, -1):
        sleep(1)
        print(c)

    pygame.mixer.init()

    pygame.mixer.music.load('rojao.wav')

    pygame.mixer.music.play()

    parar = input('Digite 0 para não ouvir os rojões')
else:
    print('Ok vaza!!!')
