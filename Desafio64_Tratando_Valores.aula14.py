## Crie um programa que leia vários números inteiros pela teclado. O programa só vai porar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag=999.)
print('~~'*17)
print('** Tratamento de vários Valores **')
print('~~'*17)
num=0
cont=0
soma=0
while True:
    num = int(input('Digite um número ou [999 para Sair]: '))
    if num != 999:
        soma += num
        cont+= 1
    else:
        print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
        exit('\nFIM DO PROGRAMA!!!')

