## Crie um programa que leia um número Real qualquer pelo teclado e mostre  na tela a sua
# porção Inteira
### Exx.: Digite um número: 6.127
### O número 6.127 tem a parte inteira  de 6


###------- Importando apenas a função matemática trunc => corta a parte inteira do número-----###
from math import trunc
num = float(input('Digite um número: '))
print('O valor real digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))

## Outra forma de fazer, é importar toda a biblioteca###
print("#-#"*20)
import math
num = float(input('Digite um número: '))
print('O valor real digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

## + uma outra forma de fazer, desta forma importa toda a biblioteca###
'''print("#-#"*20)
num = float(input('Digite um número: '))
print('O valor real digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''
