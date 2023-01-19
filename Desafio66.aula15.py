#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999 ou (0),que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

lista=[]
while True: # Quando quero ler várias vezes um comando, O comando TRUE não permite ler o 999.
    num=int(input('Digite um valor [0 para parar]: '))
    if num == 0:
        break
    #lista+=[num]
    lista.append(num) ### Podemos utilizar ambas as formas.
print(lista)
print(f'\033[1:32mA soma dos {len(lista)} valores foi {sum(lista)}!!!')

####################################################################
### Podemos fazer de duas formas.

'''cont=0
soma=0
while True: # Quando quero ler várias vezes um comando, O comando TRUE não permite ler o 999.
    num=int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont+=1
    soma+=num
print(f'\033[1:32mA soma dos {cont} valores foi {soma}!!!')'''

