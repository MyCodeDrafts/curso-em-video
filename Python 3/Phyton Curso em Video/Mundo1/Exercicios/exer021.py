import pygame

pygame.mixer.init()

pygame.mixer.music.load('ex0021.wav')

pygame.mixer.music.play()

parar = input('Digite para parar')
