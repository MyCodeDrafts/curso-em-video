#Escreva um progama que converta uma temperatura digitando em graus celsius e converta para graus fahrenheit
t = float(input('Informe a temperatura em °C: '))
nt = t * 1.8 + 32
print('A temperatura de {:.1f}°C corresponde à {:.1f}°F'.format(t, nt))
