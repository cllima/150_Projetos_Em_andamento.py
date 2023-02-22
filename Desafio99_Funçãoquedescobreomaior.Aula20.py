## Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

print('Função que descobre o maior'.center(30).upper())
print('='*30)

from time import sleep
def maior(* num): #=> * significa que vou receber vários parâmetros.
    cont=0
    print('\nAnalizando os valores passados!!')
    for valor in num:
        print(f'{valor} ',end='')
        sleep(0.5)
        cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


# Programa Principal
maior(2,9,5,6,8)
maior(5,8,4,1,3)
maior(1,2,3)
maior(6)
maior(1)