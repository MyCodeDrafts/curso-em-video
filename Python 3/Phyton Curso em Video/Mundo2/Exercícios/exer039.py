#  Faça um programa que leia o ano de um jovem e informe de acordo com sua idade:
# se ele vai se alistar ao serviço militar
# se é hora de se alistar
# se já passou do tem do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano = date.today().year - ano_nasc
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, ano, date.today().year))
if ano < 18:
    print('''Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}'''
          .format(18 - ano, (18 - ano) + date.today().year))
elif ano == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('''Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}
    '''.format(ano - 18, (18 - ano) + date.today().year))
