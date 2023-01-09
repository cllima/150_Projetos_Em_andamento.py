## Crie uma programa que leia um número inteiro e mostre na tela se ele
# é PAR ou IMPAR.

from  time import sleep
numero=int(input('Digite um número qualquer: '))
print("\033[4;31;40mANALISANDO...!!!\033[m")
sleep(2)

resultado = numero % 2
##print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O resultado é PAR: {}'.format(resultado))
else:
    print(" o resultado é ÍMPAR: {}".format(resultado))

