# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido
import random
a1 = input('Digite o nome de um aluno (a): ')
a2 = input('Digite o nome de um aluno (a): ')
a3 = input('Digite o nome de um aluno (a): ')
a4 = input('Digite o nome de um aluno (a): ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O nome do aluno (a) sorteado é {}'.format(sorteio))

