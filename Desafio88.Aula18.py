## Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
# vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.
import random

print('=' * 40)
print(f'{"Palpites para a Mega Sena":^40}'.upper())
print('=' * 40)

from time import sleep
from random import sample

jogos=[]
num=int(input("Number of GAMES: "))
for c in range(num):
    jogos.append(sample(range(1, 60), 6))
    (sleep(1))
    print(f' \033[1;32mGAME\033[35m {c+1}\033[m : {sorted(jogos[c])}') ## sorted==classificação em ordem

print('=' * 40)
(sleep(1))
print('PARABENS POR JOGAR NA MEGA SENA'.center(40))



