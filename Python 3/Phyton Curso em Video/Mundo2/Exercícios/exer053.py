#  Crie um programa que leia frase qualquer e diga se ela é um palíndromo (Frase que se pode ler de frente pra trás e de trás pra frente),
#  desconsiderando os espaços
# EX: APOS A SOPA
# A SACADA DA CASA

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):  # Da última letra, voltando 1 letra até a 1 letra
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo!')


'''frase = str(input('Digite um frase: ')).strip().upper()
cont = frase[:: -1]
print('O inverso de  {} é {} '.format(frase, cont))
if frase == cont:
    print('Temos um Palíndromo ')
else:
    print('A frase digitada não é um Palíndromo')'''
