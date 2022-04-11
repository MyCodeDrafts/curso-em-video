#  ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS
# EXTRA - KM, HECTOMETROS, DECAMETROS, DECÍMETROS E MILÍMITROS

m = float(input('Digite quantos metros você quer converter: '))
km = m / 1000
hec = m / 100
deca = m / 10
dcm = m * 10
cm = m * 100
mm = m * 100
print('Kilômetros {} km'.format(km))
print('Hectômetro: {} hm'.format(hec))
print('Decâmetro: {:.0f} decam'. format(deca))
print('Decímetro: {:.0f} dcm'.format(dcm))
print('Centímetro: {:.0f} cm'.format(cm))
print('Milímetro: {:.0f} mm'.format(mm))
