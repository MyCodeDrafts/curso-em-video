#  Desenvolva um programa que pergunte a distância de uma viagem em km e calcule o preço da passagem, cobrando
#  R$ 0,50 por km para viagens até 200km e r$ 0,45, para viagens mais longas

from time import sleep

distance = float(input('\033[7mDigite a distância em KM: \033[m'))

if distance <= 200:
    print('A sua viagem de \033[1;7;35m{}KM\033[m vai custar \033[1;36mR${:.2f}'.format(distance, distance * 0.50))
else:
    print('A sua viagem de \033[1;7;35m{}KM\033[m vai custar \033[1;36mR${:.2f}'.format(distance, distance * 0.45))

"""distance = float(input('Qual é a distância de sua viagem em KM? '))  # Forma simplificada
pr = distance * 0.50 if distance <= 200 else distance * 0.45
print('A sua viagem de {:.0f}KM vai custar R${:.2f}'.format(distance, pr))"""

