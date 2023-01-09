## Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador  e em quantos anos
# ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.
from time import sleep
y=' PROGRAMA DE FINANCIAMENTO BANCARIO '
print('-'*40)
print('\033[34m{:=^40}\033[m'.format(y))
print('-'*40)

casa=float(input('Qual o valor da Casa R$ '))
salário=float(input('Salário do comprador R$ '))
anos=int(input('Em quanto anos pretende financiar: '))
entrada=float(input('Valor da entrada R$ '))
prestação= (casa-entrada) / (anos * 12) ## Valor da casa-entrada divido pelos meses.
mínimo=salário * 0.3 # ou salário * 30/100

print('Para pagar uma casa de R$ {:.2f} com entrada de R$ {:.2f} em {} anos'.format(casa,entrada,anos), end='') # pula uma linha
print(' a prestação será de R$ {:.2f}.'.format(prestação))

#print('COMPARAÇÂO: tem que pagar R${:.2f} é o mínino é R${:.2f}.'.format(prestação,mínimo))
print('\033[33mANALIZANDO...!!!\033[m')
sleep(1.8)
if prestação <= mínimo:
    print('\033[32mAPROVADO!!! Você esta APTO para o financiamento!!\033[m\n')
else:
    print('\033[31mNEGADO!! Seu salário não permite o financiamento, pois excede os 30% do Salário!!!\033[m\n')

print('\033[34m''_'*3, 'FIM DO PROGRAMA ''_'*3)
