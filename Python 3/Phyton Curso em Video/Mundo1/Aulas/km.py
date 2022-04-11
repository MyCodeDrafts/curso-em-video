



d = float(input('Quantos km será percorrido? '))
kml = float(input('Digite o consumo do veículo em km/l: '))
vlr = float(input('Digite o valor do combustível R$: '))
c = (d / kml) * vlr
print('Em {}km, você precisará abastecer R${:.2f} '.format(d, c))

