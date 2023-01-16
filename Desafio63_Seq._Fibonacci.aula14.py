## Escreva um programa que leia um número (n) inteiro qualquer e mostre na tela os
# (n) primeiros elementos de uma Sequência de Fibonacci.
### EX.; 0 > 1 > 1 > 2 > 3 > 5 > 8
print('-'*25)
print('* SEQUÊNCIA DE FIBONACCI *')
print('-'*25)

nun=int(input('Quantos termos você quer mostrar?: '))
termo1 = 0
termo2 = 1
print('~'*25)
print(f'{termo1} -> {termo2}', end='')
cont= 3
while cont <= nun:
    termo3 = termo1 + termo2
    print(f' -> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' -> FIM!!!')
print('~'*25)