# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nome_professor = input('Olá Professor (a), digite seu nome: ')
nome_aluno = input('Nome do Aluno: ')
print(nome_professor, '***** ATENÇÃO: ***** \n Use ponto ( . ), ao invés de vírgula ( , )')
n_1 = float(input('Digite a nota do 1° Bimestre: '))
n_2 = float(input('Digite a nota do 2° Bimestre: '))

m_aluno = (n_1 + n_2) / 2
print('Professor (a) ', nome_professor, ', a média do aluno', nome_aluno, 'entre {:.1f} e {:.1f} é:\n -> {:.1f} <- '.format(n_1, n_2, m_aluno))
