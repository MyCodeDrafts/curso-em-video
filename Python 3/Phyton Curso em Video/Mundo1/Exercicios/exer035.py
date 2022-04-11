#  Desenvolva um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('\033[1;35m~*~\033[m' * 15)
print(' '*10, '\033[7;1;34mANALISADOR DE TRIÂNGULOS\033[m', ' '* 10)
print('\033[1;35m~*~\033[m' * 15)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o segundo segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')


