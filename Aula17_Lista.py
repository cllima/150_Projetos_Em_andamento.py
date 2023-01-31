#('para adicionar elemento novos na lista usar: o comando lache.append('comida') na ultima posição')
#('para adicionar em uma determinada posição usar: lanche.insert(0,'comida') ') Adiciona na posição ZERO.
#('para deletar um determindo elemento: dellanche[3]') deleta pelo número da chave
#('para deletar um determinado elemento: lanche.remove('comida')') deleta pelo nome do item.
#('para deletar o ultimo elemento: lanche.pop()') deleta o ultimo ítem da lista.
print('')
lista_lanche=['hamburgue','lanche','suco','pizza','guarana']
'''print(lista_lanche)
if 'pizza' in lista_lanche:
    lista_lanche.remove('pizza') # Removendo somente a pizza
    print(lista_lanche)'''
####################################
#valores=list(range(4,11))
####################################
'''valores=[8,9,5,1,2,7,4]
valores.sort() ## Coloca os valores de uma lista em ordem crescente
print(f'Valores em Ordem: {valores}')
valores.sort(reverse=True) ## Coloca os valores de uma lista em ordem Decrescente.
print(f'Valores em Ordem Inversa: {valores}')

print(f'Tamanho da lista: {len(valores)} ítens')
print(f'Menor: número {min(valores)},  Maior:número {max(valores)} e a Soma dos números: {sum(valores)}')'''
####################################
##Não é possível alterar uma Tupla
'''num=(2,3,9,5)
num[2] = 8
print(num)'''
####################################
## Já as Listas são Mutáveis e é possível alterar.
num=[2,3,9,5]
num[2] = 7
#print(f'Onde era 9 na lista agora passou ser Num 7:{num}')

num.append(20) ## Adicionar valor ao final da lista.
num.sort() ## Coloca a lista em ordem crescente
#num.sort(reverse=True) ## Coloca a lista em ordem Decrescente
num.insert(3,15) ## Insere o valor 15 na posição 3 da lista.

valor=int(input('Digite um número: '))
if valor in num:
    num.remove(valor) ## Remove o 1º número 2 da lista.
    print(f'Número "{valor}" Removido com Sucesso!!')
else:
    print(f'Não é posivel remover o número "{valor}", pois não consta na lista!')

#num.pop() # Deleta o último número da Lista
#num.pop(2) # Deleta o valor na posição 2 da Lista. (0,1,2,3...
print(f' {num}')

