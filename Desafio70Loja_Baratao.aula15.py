## Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# NO final, mostre:
## A) Qual o total gasto na compra R$.
## B) Quantos produtos custam mais de R$ 1.000,00.
## C) Qual é o produto mais barato R$.
print('='*25)
print('       LOJA BARATÃO ')
print('='*25)
lista1=[]
lista2=[]
cont=0
while True:
    prod=str(input('Nome do Produto: ')).strip().upper()
    preco=int(input('Preço R$ '))
    print('-' * 25)
    opcao = str(input('Quer continuar comprando [S/N]: ')).strip().upper()
    if opcao == 'n':
        print('COMPRA FINALIZADA. VOLTE SEMPRE!!!')
        break
        lista1.append(prod)
        lista2.append(preco)
        cont+=1

        print(f'O total da compra foi R$ {sum(lista2):.2f}. \nTemos {len(lista1)} produtos que custam mais de R$ {max(lista2):.2f}. '
              f'\nO produto mais barato foi a {cont} que custa R$ {min(lista2):.2f}. ')
    print('=' * 25)
