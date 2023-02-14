## Aorimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.
print('=' * 50)
print(f'{"Cadastro de Jogador de Futebol":^40}'.upper())
print('=' * 50)
time=[]
jogador={}
partidas=[]

while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do Jogador: '))
    total=int(input(f'Quantas partidas "{jogador["Nome"]}" jogou: '))
    partidas.clear() ## Serve para esvaziar a lista e não duplicar as informações.

    for c in range(total):
        partidas.append(int(input(f' << Quantos gols na {c+1}ª partida: ')))
    jogador['Gols'] = partidas[:] ### Jogador['gols'] recebe uma copia de partidas, ou seja, coloca a lista partida dentro do Dicionário.
    jogador['Total'] = sum(partidas) ## total vai para o Dicionário já com a Soma.
    time.append(jogador.copy())
    print('-' * 50)
    while True:
        resp=str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Responda Sim ou Não.')
    if resp == 'N':
        break
  ## Da qui pra cima a 1ª parte

print('='*50)
## Fazendo o Cabeçalho
print('Código   ', end='') ## Como o Códgo não esta dentro do Dicionário, tem que fazer um for
for i in jogador.keys():
    print(f'{i:<18}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3}      ', end='')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('='*50)

# Mostrar os dados:
while True:
    busca=int(input('Dados de qual Jogador [999 FECHAR]: '))
    print('*-' * 25)
    if busca == 999:
        break
    if busca >= len(time): ## Se a busca for maior que o número de jogador no Time da ERRO.
        print(f'ERRO!! NÂO Existe Jogador com este código "{busca}"!')
    else:
        print(f'<<< LEVANTAMENTO DO JOGADOR => "{time[busca]["Nome"]}" >>>'.center(50).upper())
        print('-' * 50)
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No {i+1}º jogo fez {g} gols.')

    print('=' * 50)
exit(f'<<<<<<>>>>>> VOLTE SEMPRE <<<<<<>>>>>>'.center(50))
