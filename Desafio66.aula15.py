#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999,que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).
num=0
cont=0
soma=0

while True:
    num=int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont+=1
    soma+=num
print(f'\033[1:32mA soma dos {cont} valores foi {soma}!!!')
