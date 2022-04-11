# Desafio 038
# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR, OS DOIS VALORES SÃO IGUAIS



print('*-*-' * 10)
print(' ' * 3, 'Comparison of whole numbers!')
print('*-*-' * 10)
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
if first_number > second_number:
    print('{} is greater than {}.'.format(first_number, second_number))
elif first_number < second_number:
    print('{} is greater than {}'.format(second_number, first_number))
else:
    print('{} and {} they are the same!'.format(first_number, second_number))