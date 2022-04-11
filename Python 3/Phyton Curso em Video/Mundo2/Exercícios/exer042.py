#  Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero todos os lados são iguais
# Isósceles dois lados iguais
# Escaleno todos os lados diferentes
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
fórmula = a < b + c and b < a + c and c < a + b
if fórmula and a == b == c:
    print('Os segmentos podem formar um triângulo EQUILÁTERO!')
elif fórmula and a == b != c or a != b == c or a == c != b:
    print('Os segmentos podem formar um triângulo ISÓSCELES!')
elif fórmula and a != b != c != a:
    print('Os segmentos podem formar um triângulo ESCALENO!')
else:
    print('Os segmentos não podem formar um triângulo!')
