#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.
print('Funções para sortear e somar'.center(30).upper())
print('='*30)

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da Lista')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n) #Sorteia números entre 1 e 10.
        print(f'{n} ', end='')
        sleep(0.5)
    print('\nFIM!!!')

def somarPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma+= valor
    print(f'Somando so valores PARES dos números {lista}, temos a SOMA = {soma}')

# Programa Principal
numeros=[]
sorteia(numeros)
somarPar(numeros)

