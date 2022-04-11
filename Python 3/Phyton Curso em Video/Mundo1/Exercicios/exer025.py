#  Crie um programa que leia o nome inteira de uma pessoa e diga se ela tem 'Silva' no nome

nome = str(input('Digite seu nome completo: ')).title().strip()
s = nome.title().strip()
print('Seu nome tem Silva? ', 'Silva' in nome)

#  nome = str(input('Qual é o seu nome completo?: '))
#  print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))

