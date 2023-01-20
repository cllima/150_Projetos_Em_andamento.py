## Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar Comprando.
# NO final, mostre:
## A) Qual o total gasto na compra R$.
## B) Quantos produtos custam mais de R$ 1.000,00.
## C) Qual é o produto mais barato e o preço R$.
## D) Qual o produto mais caro e o preço R$.
## E) Quantidade de ítens comprado

print('{:=^40}'.format(' LOJA BARATÃO v2 '))
print('{:=^40}'.format(' ESTATISTICA DE DADOS EM PRODUTOS '))
print('='*40)

lista_prod=[]
lista_preço=[]
pr_m_mil=0  #preço maior que Mil
barato=0 # Produto mais barato
caro=0 # Produto mais Caro

while True:
    prod=str(input('Qual o PRODUTO: ')).strip().upper()
    lista_prod.append(prod)

    preço=float(input('PREÇO: R$ '))
    lista_preço.append(preço)

    if preço > 1000:
        pr_m_mil+=1
    if prod:
        barato = lista_preço.index(min(lista_preço))
    if prod:
        caro = lista_preço.index(max(lista_preço))

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar Comprando [S/N]: ')).strip().upper()[0]
        print('-'*40)

    if resp == 'N':
        break
print('{:-^40}'.format(' COMPRA FINALIZADA '))
print('{:=^40}'.format(' VOLTE SEMPRE!! '))

print(f'\nO TOTAl gasto na compra foi de R$ {sum(lista_preço):.2f} '
      f'\nTemos {pr_m_mil} produto(s) que custa(m) mais de R$ 1.000,00 '
      f'\nO produto mais BARATO da Lista de Compra foi a(o) \033[1:32m{lista_prod[barato]}\033[m e custa R$ {min(lista_preço):.2f}'
      f'\nO produto mais CARO da Lista de Compra foi a(o) \033[1:32m{lista_prod[caro]}\033[m e custa R$ {max(lista_preço):.2f}'
      f'\nTemos um TOTAL de {len(lista_prod)} ítens Comprado.')