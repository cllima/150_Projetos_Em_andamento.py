'''print('Fazendo uma LISTA!!')
lista = []
for c in range(0,4):
    lista.append(int(input(f'Digite o {c}º Valor da Lista: ')))
print(f'A lista tem os números {lista}.')
print('='*30)

for c, num in enumerate(lista): ## enumerate pega o C e o V.
    print(f'Na posição {c} encontrei o valor {num}.')
print('Cheguei ao FINAl da Lista!!!')'''

######################################################
a = [2,3,5,6]
#b = a # Cria uma ligação entre A e B
b = a[:] # Ao colocar [:] faz uma copia da lista A em B.
b[2]=8 # altera a posição 2.
print(f'Lista A:{a}')
print(f'Lista B:{b}')
