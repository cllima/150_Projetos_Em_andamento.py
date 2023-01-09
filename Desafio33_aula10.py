## Faça um programa que leia três números e mostre qual é o maior e qual e o menor.
from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

print("ANALIZANDO...!")
sleep(1)
lista=[a,b,c]
print('O MAIOR valor digitado foi {}.'.format(max(lista)))
print('O MENOR valor digitado foi {}.'.format(min(lista)))

## Outra forma de fazer:
# Analizando o menor valor:
'''menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(' '.format(menor))

# Analizando o maior valor:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("ANALIZANDO...!")
sleep(1)
print('O menor valor digitado foi {:.0f}'.format(menor))
print('O maior valor digitado foi {:.0f}'.format(maior))'''
