## Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
## de um triângulo retântulo, calcule e mostre  o comprimento da hipotenusa.

## Maneira tradicional de fazer sem importar Biblioteca.
'''co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hi=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

print('#-#'*15)
## Importando a Biblioteca da hypot
import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))