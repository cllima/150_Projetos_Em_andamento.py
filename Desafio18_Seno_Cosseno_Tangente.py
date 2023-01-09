## Faça um programa que leia um ângulo qualquer e mostre na tela o valor
## do seno, cosseno  e tangente desse ângulo.

import math
ângulo=float(input('Digite o ângulo que você deseja: '))
seno=math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente=math.tan(math.radians((ângulo)))
print('O ângulo de {} tem a TANGENTE de {:.2f} '.format(ângulo, tangente))

print('##---##'*2)
## Importando apenas as Bibliotecas individuais.

from math import radians,sin,cos,tan
angulo=float(input('Digite o Ângulo: '))
seno=sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno=cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente=tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))





