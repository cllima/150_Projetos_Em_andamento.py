## Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados.
## Expl.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero=int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
##print('Analizando o número {} '.format(numero))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {} \n'.format(u,d,c,m))

fim=' FIM DO PROGRAMA '
print('{:=^35}'.format(fim))
print('='*35)







