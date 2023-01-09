## Faça um programa que leia um número Inteiro e mostre
# na tela o seu sucessor e o seu antecessor.

from time import sleep
n=int(input('Digite um número: '))
a=n-1
s=n+1

print('\033[34m PROCESSANDO...\033[m')
sleep(2)
print('O antecessor do número {}: \né {}, e seu sucessor é o número {}.'.format(n,a,s))

###==== Outra forma de Fazer ===###
print('Analizando o numero {}, o Antecessor seria {}, e o seu Sucessor {}. '.format(n,(n-1),(n+1)))


