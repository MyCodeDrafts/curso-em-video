nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Johnny' or nome == 'Jéssica' or nome == 'Jessica':
    print('Ual... Que nome lindo você tem {}'.format(nome))
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('O nome {}, é popular no Brasil'.format(nome))
elif nome in 'Ana Cláudia Roberta': # Condições que estão dentro do nome "Se na variável tiver : 'Ana Cláudia Roberta '
    # excutar o bloco"
    print('Belo nome feminino {}'.format(nome))
else:
    print('Seu nome não tem nada de mais {}'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))