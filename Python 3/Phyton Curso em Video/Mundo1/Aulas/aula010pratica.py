# Condição simples
"""nome = str(input('Qual é o seu nome: '))
if nome == 'Jéssica':  # Criou essa condição
    print('Que nome lindo você tem!'.format(nome))  # Esse só acontece se ocorrer a condição acima
print('Olá {}.'.format(nome))"""


# Condicão composta
nome = str(input('Qual é o seu nome? '))
if nome == 'Jéssica':
    print('Olá {}!!! Que nome lindo você tem!!'.format(nome))
else:
    print('Olá {}. Seu nome é tão normal'.format(nome))


"""n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 5:
    print('Sua média de {:.1f} é BOA. PARABÉNS!!'.format(m))
else:
    print('Sua média de {:.1f} é RUIM. ESTUDE MAIS!!!'.format(m))"""


