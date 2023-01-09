## Escreva uma programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima  do limite = Calcular valor
'''from emoji import emojize
print(emojize('\nVc excedeu o limite de velocidade :car:  :police_car:.'
              '\nSerá multado em R${:.2f} :money_with_wings:'.format((velocidade - 80) * 7.0), use_aliases=True))'''


import time
horaAtual=time.strftime('%H:%M',time.localtime())
print(horaAtual)

velocidade=float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa= 7.00*(velocidade-80)
    print('MULTADO!!'
    '\nVocê excedeu o limite permitido de 80km/h., o valor da multa é de R${:.2f}.'.format(multa))


if horaAtual >= '05:00' and horaAtual <= '12:00':
    print('Tenha um Bom Dia! Dirija com segurança!!')
elif horaAtual > '12:00' and horaAtual <= '17:59':
    print('Tenha uma Boa Tarde! Dirija com segurança!!')
else:
    print('Tenha uma Boa Noite! Dirija com segurança!!')






