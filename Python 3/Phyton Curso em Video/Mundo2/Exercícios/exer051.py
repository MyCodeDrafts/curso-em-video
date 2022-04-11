#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

'''termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
formula = termo + (10 - 1) * razão
for c in range(0, formula + 1, 2):
    print('{} ' .format(c), end=' -> ')
print('Acabou')'''


termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('Acabou')