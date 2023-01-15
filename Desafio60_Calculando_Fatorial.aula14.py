## Faça um programa que leia um número qualquer e mostre o seu Fatorial.
# ex.: 5!=5x4x3x2x1 = 120
y=' CALCULADO O FATORIAL '
print('_'*40)
print('\033[32m{:=^40}\033[m'.format(y))
print('-'*40)

#Usando 'for'
num=int(input('Digite um número para calcular o Fatorial: '))
cont = num
f = 1
print(f'CALCULANDO {num}! = ',end='')
for num in range(1, num + 1):
    print(f'{cont}', end=' ')
    print('x 'if cont > 1 else '= ', end='')
    f *= cont
    cont -= 1
print(f'{f}')

#Usando While
'''num=int(input('Digite um número para calcular o Fatorial: '))
cont = num
f = 1
print(f'CALCULANDO {num}! = ',end='')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x 'if cont > 1 else '= ', end='')
    f *= cont
    cont -= 1
print(f'{f}')'''

#Usando Factorial
## Usando a Biblioteca
'''from math import factorial
num=int(input('Digite um número para calcular o Fatorial: '))
f = factorial(num)
print(f'O FATORIAL de {num} e {f}.')'''

