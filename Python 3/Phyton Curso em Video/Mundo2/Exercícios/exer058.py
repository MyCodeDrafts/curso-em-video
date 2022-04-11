import random

print('= ' * 12)
print(' ' * 5, 'ADIVINHAÇÃO')
print('= ' * 12)
print('   Vou escolher um número entre 0 e 10   \ntente adivinhar')
pc = random.randint(0, 10)
player = 0
palpite = 0
while player != pc:
    player = int(input('   Qual seu palpite: '))
    palpite += 1
    if player < pc:
        print('ERRADO, é um número maior! Tente novamente: ')
    elif player > pc:
        print('ERRADO, é um número menor! Tente novamente:')
    else:
        print('  ACERTOU')

print(f'    Foi um no {palpite}° palpite!')