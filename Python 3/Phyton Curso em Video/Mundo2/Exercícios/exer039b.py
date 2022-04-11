# DESAFIO 039
# FAÇA UM PROGRAMA QUE LEIA O ANO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE:
# SE ELE VAI SE ALISTAR AO SERVIÇO MILITAR
# SE É HORA DE SE ALISTAR
# SE JÁ PASSOU DO TEM DO ALISTAMENTO
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import date
print('* * ' * 7)
print(' ' * 3, 'Alistamento Militar'.upper())
print('* * ' * 7)
ano_nascimento = int(input('Digite sua o ano do seu nascimento: '))
idade_atual = date.today().year - ano_nascimento
idade_alistamento = 18

print('Quem nasceu em {}, tem {} anos em {}'.format(ano_nascimento, idade_atual, date.today().year))
if idade_atual < idade_alistamento:
    # Idade de alistamento e subtrair pela idade atual
    print('Ainda faltam {} anos para o alistamento.'.format(idade_alistamento - idade_atual))
    # Ano de alistamento + ano atual para informar quando será o alistamento
    print('Seu alistamento será em {}.'.format((idade_alistamento - idade_atual) + date.today().year))
elif idade_atual == idade_alistamento:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade_atual > idade_alistamento:
    # Diferença entre idade atual e idade de alistamento
    print('Você já deveria ter se alistado em há {} anos'.format(idade_atual - idade_alistamento))
    # Data atual - a diferença de anos de alistamento
    print('Seu alistamento foi em {}'.format(date.today().year - (idade_atual - idade_alistamento)))
