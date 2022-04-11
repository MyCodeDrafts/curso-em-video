#  Crie um programa que faça o computador jogar Jokenpô com você
import time
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('''Vamos jogar um JOGO?!?!?!
\033[1;4;36m0\033[m   \033[1;35mPEDRA\033[m 
\033[1;4;36m1\033[m  \033[1;35mPAPEL\033[m
\033[1;4;36m2\033[m  \033[1;35mTESOURA\033[m
\033[1;4;46mQual é sua jogada: \033[m'''))
time.sleep(1)
print('\033[1;36mJO')
time.sleep(1)
print('\033[1;36mKEN')
time.sleep(1)
print('\033[1;36mPÔ !!!\033[m')
print('=-=' * 10)
print(' ' * 20, '\033[1;34mEu joguei {}\033[m'.format(itens[computador]))
print(' ' * 20, '\033[1;34mVocê jogou {}\033[m'.format(itens[jogador]))
print('=-=' * 10)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE')
    elif jogador == 1:
        print('\033[1;36mVENCEU')
    elif jogador == 2:
        print("\033[1;31;4mVENCI")
    else:
        print('\033[4;1mJogada inválida\033[m. \033[1;31mTA MOSCANDO?\033[m')
        if computador == 1:  # Computador jogou PAPEL
            if jogador == 0:
                print('\033[1;4;31mVENCI')
            elif jogador == 1:
                print('EMPATE')
            elif jogador == 2:
                print('\033[1;36mVENCEU')
            else:
                print('\033[4;1mJogada inválida\033[m. \033[1;31mTA MOSCANDO?\033[m')
            if computador == 2:  # Computador jogou TESOURA
                if jogador == 0:
                    print('\033[1;36VENCEU')
            elif jogador == 1:
                print('\033[1;4;31mVENCI')
            elif jogador == 2:
                print('\033[1;33mEMPATE')
            else:
                print('\033[4;1mJogada inválida\033[m. \033[1;31mTA MOSCANDO?\033[m')
