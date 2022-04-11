a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o segundo segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')