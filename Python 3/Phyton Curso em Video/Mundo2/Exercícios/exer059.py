# Desafio 059
# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair
# Seu programa deverá realizar a operação solicitada em cada caso.
import time

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
opcao = int(input('Qual é sua opção:\n[1] somar\n[2] multiplicar \n[3] compação \n[4] novos números\n[5] sair\nEscolha uma opção: '))

i = 0

while opcao <= 0 or opcao > 5:
    print('OPÇÃO INVÁLIDA')
    time.sleep(1)
    print('Tente novamente')
    time.sleep(1)
    opcao = int(input(
        'Qual é sua opção:\n[1] somar\n[2] multiplicar \n[3] maior \n[4] novos números\n[5] sair\nEscolha uma opção: '))
if opcao == 4:
    print('Escolha novamente')
    primeiro_numero = int(input('Primeiro número: '))
    segundo_numero = int(input('Segundo número: '))
if opcao == 1:
    soma = primeiro_numero + segundo_numero
    print(f'A soma entre {primeiro_numero} e {segundo_numero} é igual a {soma}')
elif opcao == 2:
    multiplicacao = primeiro_numero * segundo_numero
    print(f'A multiplicação entre {primeiro_numero} e {segundo_numero} é igual a {multiplicacao}')
elif opcao == 3:
    if primeiro_numero > segundo_numero:
        print(f'O {primeiro_numero} é maior que {segundo_numero}')
    elif primeiro_numero < segundo_numero:
        print(f'O {primeiro_numero} é menor que {segundo_numero}')
    else:
        print('Os números são iguais!')
if opcao == 5:
    print('Obrigado, e volte sempre!')


