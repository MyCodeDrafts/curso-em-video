#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
#  de acordo com sua idade:
# Até 9 anos mirim:
# Até 14 anos Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima de 25 anos: Master

from datetime import date
print('Para saber a categoria de um atleta, informe ')
ano = int(input('Ano nascimento do atleta: '))
categoria = date.today().year - ano
print('O Atleta tem {} anos'.format(categoria))
if categoria <= 9:
    print('Categoria: \033[1;31mMIRIM')
elif categoria <= 14:
    print('Categoria \033[1;31mINFANTIL')
elif categoria <= 19:
    print('Categoria \033[1;31mJÚNIOR')
elif categoria <= 25:
    print('Categoria \033[1;31mSÊNIOR')
elif categoria > 25:
    print('CATEGORIA \033[1;31mMASTER')
