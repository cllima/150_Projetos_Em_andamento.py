## Crie um programa que vai gerar 6 números aleatórios e colocar em uma tupla.
## Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
## valor que estão na tupla.
print(f'='*63)
print('{:*^63}'.format('    NÚMEROS DA MEGA SENA    '))
print(f'='*63)

from random import sample ## Usando sample em vez de randint

num = tuple(sample(range(60),6))

print(f'Os números sorteados da MEGA SENA foram: {sorted(num)}') # sorted coloca em ordem
print(f'\nO MENOR número sorteado foi: {min(num)} e o MAIOR número sorteado foi: {max(num)}.')

