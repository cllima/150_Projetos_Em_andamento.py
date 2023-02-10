## Crie um programa onde 4 jogadores joguem um Dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o MAIOR número no Dado.
print('=' * 40)
print(f'{"Jogo de Dados em Python":^40}'.upper())
print('=' * 40)
from random import randint
from time import sleep
#from operator import itemgetter
jogo = {'jogador1': randint (1,6),
        'jogador2': randint (1,6),
        'jogador3': randint (1,6),
        'jogador4': randint (1,6)}
ranking =()
print('Valores Sorteados')

for k,v in jogo.items():
    print(f'{k} tirou {v} no Dado.')
    sleep(.8)
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True) ## item(1) coloca em ordem de valor
print('='*40)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(.8)
print('\n<<< PROGRAMA FINALIZANDO >>>'.center(40))
