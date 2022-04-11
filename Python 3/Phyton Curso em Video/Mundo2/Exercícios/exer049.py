#  Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher
#  Só que agora utilizando um laço for

n = int(input('Digite um número para saber a sua tabuda: '))
print('-' * 20)
for c in range(1, 11):
    print('{}   x   {:2}  =  {}'.format(n, c, n * c))
print('-' * 20)
