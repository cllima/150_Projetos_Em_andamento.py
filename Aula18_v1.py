###
'''dados=list()
dados.append('Pedro')
dados.append(25)
print(dados)
print(f'O primeiro nome é: {dados[0]} e sua idade {dados[1]} anos.')'''

###########################
## Lista composta, lista dentro de lista.
pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas)
print(f'O primeiro Nome: {pessoas[0][0]}')
print(f'Idade do segundo Nome: {pessoas[1][1]}')
print(f'Terceiro nome: {pessoas[2][0]}')
print(f'Nome e Idade: {pessoas[1]}')