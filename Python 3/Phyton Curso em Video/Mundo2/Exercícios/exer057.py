# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso eteja errado, peça a digitação  novemente até ter um valore correto

sexo = 0
while sexo != 'M' and 'F':
    sexo = str(input('Informe seu sexo [M/F] ')).upper().strip()
    if sexo != 'M' and 'F':
        print('OPÇÃO INVÁLIDA, Por favor,', end='')
print('Sexo {} registrado com sucesso!'.format(sexo))