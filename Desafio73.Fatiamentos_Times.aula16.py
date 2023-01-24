## Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
## na ordem de colocação. Depois mostre:
#A) Os 5 primeiros colocados.
#B) OS últimos 4 colocados da Tabela.
#C) Uma lista com os Times em ordem alfabética.
#D) Em que posição está o Time da Fluminense.,
# OBS.: Pegar a Tabela do Campeonato np Google.
print('{:=^80}'.format(' Tabela do CAMPEONATO BRASILEIRO - 2022 '))
print('=' * 80)

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
             'Athético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo',
             'Santos', 'Goiás', 'Bragantino', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude', 'Coritiba')

print(f'\nTabela de Classificação do Brasileirão::  \n{times}.')
print(f'\nOs 5 primeiros colocados são:\n{times[:5]}')
print(f'\nOs últimos 4 colocados da Tabela são:\n{times[-4:]}')
print(f'\nLista com os Times em ordem alfabética:\n{sorted(times)}')
print(f'O time do Fluminense está na {times.index("Fluminense")+1}ª posição.')