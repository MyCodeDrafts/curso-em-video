#  for c in range(0, 6):  # repetição 06 vezes
#        print('Oi')
#        print('Fim')
'''for c in range(6, 0, -1):  # Contagem ao contrário
    print(c)
print('FIM')'''
'''for c in range(0, 7, 2):   # Pulando de 2 em 2
    print(c)
print('fim')'''
'''n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('Fim')'''
'''i = int(input('Início:  '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):  # Faz a contagem do início ao fim do número digitado 
    print(c)
print('Fim')'''
'''for c in range(0, 4):
    n = int(input('Digite um número: '))  # Faz a repetição da variável de 0 a 4 vezes
print('fim')'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
