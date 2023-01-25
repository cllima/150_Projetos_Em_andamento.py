print('<<< ALTERANDO VALORES DE UMA LISTA DE PREÇO >>>')
print('')
lista_preço=[1000,500,200,100,50,25]
print(f'Lista de Preço Atual R$ {lista_preço}.')
nova_lista_preço=[]

print('Lista de preço com aumento de 50% R$', end=' ')
for preço in lista_preço:
    nova_lista_preço.append(preço*1.50) ## Aumento de 50% nos preços
print(nova_lista_preço)
