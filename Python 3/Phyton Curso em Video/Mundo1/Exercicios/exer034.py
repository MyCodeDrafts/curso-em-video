#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#  Para salários superiores a R$1250,00, calcule um aumento de 10%
#  Para inferiores ou iguais, o aumento é de 15%


salário = float(input('Digite o salário do funcionário R$ '))
if salário >= 1250.00:
    print("""'O aumento será de \033[1;33m10%\033[m ficando um total de \033[1;31mR${:.2f}\033[m'"""
          .format(salário + (salário * 10 / 100)))
else:
    print("""'O aumento será de \033[1;33m15%\033[m ficando um total de \033[1;31mR${:.2f}0\33[m'"""
          .format(salário + (salário * 15 / 100)))

#  Resolução do professor:
"""s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, novo))"""
