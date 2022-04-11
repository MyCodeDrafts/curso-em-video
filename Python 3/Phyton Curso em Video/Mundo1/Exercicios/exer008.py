#Escreva um programa que leia um valor em metros e o exiba convertido:
#em centímetros e milímetros
# Extra - km, hm, decametros, decimetros centímetros e milímetros
metros = float(input('Digite a quantidade em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = (metros * 100)
mm = (metros * 1000)
print('Veja a quantidade de {}m, em: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '.format(metros,km, hm, dam, dm, cm, mm))
