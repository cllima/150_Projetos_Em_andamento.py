## Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# NO final, mostre:
## A) Qual o total gasto na compra R$.
## B) Quantos produtos custam mais de R$ 1.000,00.
## C) Qual é o produto mais barato R$.

print('{:=^40}'.format(' LOJA BARATÃO '))
print('{:=^40}'.format(' ESTATISTICA DE DADOS EM PRODUTOS '))
print('='*40)

total_compra=0
total_mil=0
menor=0
cont=0
barato=''
while True:
    prod=str(input('Nome do Produto: ')).strip().upper()
    preco=float(input('Preço: R$ '))
    cont+=1

    total_compra+=preco
    if preco > 1000:
        total_mil+=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod

    print('-' * 40)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar comprando [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break
print('{:-^40}'.format(' COMPRA FINALIZADA COM SUCESSO '))
print('{:=^40}'.format(' VOLTE SEMPRE!! '))
print(f'\nO total gasto na COMPRA R$ {total_compra:.2f} '
      f'\nTemos {total_mil} produto que custa mais de R$ 1.000,00 '
      f'\nO produto mais barato foi {barato} e custa R$ {menor:.2f}')






