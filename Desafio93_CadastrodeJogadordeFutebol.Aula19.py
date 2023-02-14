# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato.
print('=' * 40)
print(f'{"Cadastro de Jogador de Futebol":^40}'.upper())
print('=' * 40)

jogador={}
partidas=[]

jogador['nome']=str(input('Nome do Jogador: '))
total=int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for c in range(total):
    partidas.append(int(input(f' << Quantos gols na {c+1}ª partida: ')))
jogador['gols'] = partidas[:] ### Jogador['gols'] recebe uma copia de partidas, ou seja, coloca a lista partida dentro do Dicionário.
jogador['total'] = sum(partidas) ## total vai para o Dicionário já com a Soma.

print('='*40)
print(jogador)
print(partidas)
print('='*40)

for k,v in jogador.items(): ## items pega do Dicionário
    print(f'O campo {k} tem o valor {v}.')
print('='*40)
##print(f'O jogador {jogador["nome"]}, jogou {total} partidas.') ## Pode ser feito de ambas a formas.
print(f'O jogador {jogador["nome"]}, jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']): ## Mostrar os gols de cada partida => enumerate pega da Lista.
    print(f'  => Na {i+1}ª partida, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
