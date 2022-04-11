# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso eteja errado, peça a digitação  novemente até ter um valore correto

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0] # Pegar só 1ª letra
print('Sexo {} registrado com sucesso'.format(sexo))
