#Faça um algoritmo que leia o salário de um funcionário e mostre seu salário, com 15% de aumento
salário = float(input('Digite o salário do funcionário R$: '))
novo_salário = salário + (salário * 15 / 100)
print('O salário com aumento de 15% é R$ {:.2f}'.format(novo_salário))

