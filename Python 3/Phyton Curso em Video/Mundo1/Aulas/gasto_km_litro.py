km = float(input('Digite quantos km vai percorer km '))
km_l = float(input('Digite quantos km/l o veículo faz km/l '))
vc = float(input('Digite o preço do combustível por litro: R$ '))
calc = (km / km_l) * vc
calc2 = km / km_l
print('Em {}km, com o veículo fazendo {}km/l, você precisará abastecer R${:.2f} ou {:.2f}l'.format(km, km_l, calc, calc2))
