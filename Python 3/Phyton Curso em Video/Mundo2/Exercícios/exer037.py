#  Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 = para binário
# 2 = para octal
# 3 = para hexadecimal

n = int(input('Digite um número inteiro '))
print("""Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
[0] Para sair""")
esc = int(input('Sua opção: '))

if esc == 1:
    print('{} convertido BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(n, oct(n)[2:]))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(n, hex(n)[2:10]))
elif esc == 0:
    print('Adios Muchacho(a)!')
else:
    print('Opção inválida!!')
