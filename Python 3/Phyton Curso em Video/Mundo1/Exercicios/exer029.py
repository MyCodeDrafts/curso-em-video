#  Escreva um progama que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#  foi multado. A multa vai custar R$ 7,00 por cada km acima do limite
from time import sleep
print("""\033[7;1;40mOlá, essa estrada tem limite de velocidade de \033[0;1;31m80km!!!/h\033[m\033[7;40mSe você\033[m
\033[7;40;1multrapassar essa velocidade será multado em R$ 7.00 por km acima do limite!!\033[m """)
vel_carro = float(input('\033[1;34mDigite a velocidade do carro: km/h \033[m'))
print('\033[1;31mANALISANDO VELOCIDADE!!!\033[m')
sleep(3)
if vel_carro > 80:
    print("""\033[1;31mMULTADO!!!\033[m 
    \033[1;35mVocê excedeu o limite permitido que é de 80km/h. Você deve pagar uma multa de\033[m 
    \033[1;31mR${:.2f}\033[m""".format((vel_carro - 80)*7))
else:
    print('\033[7;34mTenha uma ótima viagem, dirija com segurança!\033[m')
