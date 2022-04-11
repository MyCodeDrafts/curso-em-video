#  OS comandos que estiverem colado no lado esquerdo da tela vai ser executado sempre.
#  Os comandos que estiverem alinhado, podem ser executados ou não, depende da situação
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
   print('Carro novo')
else:
    print('Carro Velho')
print('------ FIM -------')

#  Condição simplificada
#tempo = int(input('Quantos anos tem seu carro?: '))
#print('Carro Novo'if tempo <= 3 else 'Carro Velho')
#print('---> FIM <---')