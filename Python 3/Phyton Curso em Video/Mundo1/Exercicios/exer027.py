# Faça um programa que leia o nome competo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente. EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).title().strip()
primeiro = nome.split()
print('Seu primeiro nome é {}'.format(primeiro[0]))
print('Seu ultimo nome é {}'.format(primeiro[-1]))
#  print('Seu último nome é {}.'.format(nome[len(nome)-1]))


