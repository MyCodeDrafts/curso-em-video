#  Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando no final de acordo
#  com a média atingida:
# Média abaixo de 4.9: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado
import time

print('Digite abaixo as notas para saber se o aluno está \033[1;31mAPROVADO(A), REPROVADO(A) ou RECUPERAÇÃO\033[m')
time.sleep(1)
n1 = float(input('Digite a primeira nota: '))
time.sleep(1)
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
time.sleep(1)
if média <= 4.9:
    print('Com média de {:.1f}, o aluno(a) está \033[1;31mREPROVADO (A)\033[m!!'.format(média))
elif 5.0 <= média <= 6.9:
    print('Com média de {:.1f}, o aluno(a) está de  \033[1;33mRECUPERAÇÃO\033[m!!'.format(média))
elif média >= 7.0:
    print('Com média de {:.1f}, o aluno(a) está \033[1;34mAPROVADO(A)\033[m!!'.format(média))
