# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for d in range(1, 5):
    print('---- {} ---- Pessoa'.format(d))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper().strip()
    somaidade += idade
    if d == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))