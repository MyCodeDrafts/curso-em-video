#Crie um progrma que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar considere U$$1,00 = R$3,27
n = float(input('Olá, digite quanto dinheiro você tem na carteira: R$ '))
print('Com R${:.2f}, você pode comprar U$${:.2f}'.format(n, n / 3.27))

