'''pessoas={'nome':'Clayton Lima','idade':25,'sexo':'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos é do sexo {pessoas["sexo"]}.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
'''for k in pessoas.keys():
    print(k)'''
######################################################
'''del pessoas['sexo'] ## Apaga o elemento sexo M.
pessoas['sexo']='F' ## Adiciona no Dicionário sexo F
pessoas['peso']= 88.5 ## Adiciona no Dicionário o peso.
pessoas['nome']= 'Marcela' # Altera o nome do Dicionário
for k,v in pessoas.items():
    print(f'{k}{v:.>16}')'''
######################################################
print('Criando um Dicionário dentro de uma Lista')
print()
'''brasil = [] ## Lista
estado1={'uf':'São Paulo','sigla':'SP'} ## Dicionário
estado2={'uf':'Rio de Janeiro','sigla':'RJ'}  ## Dicionário

brasil.append(estado1) # Colocando o estado1 na lista Brasil
brasil.append(estado2)

print(brasil)
print(brasil[0]) # Mostra São Paulo
print(brasil[1]) # Mostra Rio
print(brasil[0]['uf'])
print(brasil[0]['sigla']) '''

estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  ## .copy() faz uma copia
#print(brasil)
print()
for e in brasil: ## Este for é da LISTA
    for v in e.values(): # Este for e do Dicionário
        print(v, end=' ')
    print()
