#  DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA

na = str(input('Para saber a média do aluno digite o nome aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média do aluno \033[4;36m{}\033[m é \033[1;31m{}'.format(na, (n1 + n2) / 2))

