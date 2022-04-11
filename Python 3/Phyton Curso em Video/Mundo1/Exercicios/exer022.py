#  Crie um programa que leia o nome completo de uma pessoa e mostra:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar os espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas {} '.format(nome.upper()))
print('Seu nome com todas as letras minúsculas {}'.format(nome.lower()))
letras = nome.split()
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))  # Usa o count para contador de espaços
print('Seu primeiro nome é {} e tem {} letras'.format(letras[0], len(letras[0])))
"""print('Seu primeiro nome tem {} Letras'.format(nome.find(' ')))"""  # Usando o find pra encontrar os espaços

