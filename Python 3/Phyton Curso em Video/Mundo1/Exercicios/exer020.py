# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = str(input('Digite o nome do aluno (a): '))
a2 = str(input('Digite o nome do aluno (a): '))
a3 = str(input('Digite o nome do aluno (a): '))
a4 = str(input('Digite o nome do aluno (a): '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem dos alunos (as) para apresentação será: ')
print(lista)
