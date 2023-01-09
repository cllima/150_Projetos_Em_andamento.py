## Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario=float(input('Digite o valor do Salário R$ '))
aumento=salario + (salario*15/100)
print('Um salário de R$ {:.2f}, com o aumento proposto de 15%, ficará R$ {:.2f}'.format(salario, aumento))

