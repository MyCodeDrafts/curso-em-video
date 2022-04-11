#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC é de {:.1f} kg/m²'.format(imc))
if 18.5 <= imc < 25:
    print('Você está \033[1;31mABAIXO DO PESO')
elif imc <= 25:
    print('Você está com \033[1;33mPESO NORMAL')
elif imc <= 30:
    print('Você está \033[1;33mSOBREPESO')
elif imc <= 40:
    print('Você está \033[1;31mOBESO')
elif imc >= 40:
    print('Você está com \033[4;31;1mOBESIDADE MÓRBIDA')
