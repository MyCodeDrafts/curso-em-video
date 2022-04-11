#  Estrutura condicional aninhadas:
nome = str(input('Qual é o seu nome: ')).title() # .title, deixa a primeira Letra maiúscula
if nome == 'Johnny':
    print('Que nome bonito!!')
elif nome == 'João' or nome == 'José' or nome == 'Maria':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Jéssica':
    print('Belo nome Tchuchuca: ')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
