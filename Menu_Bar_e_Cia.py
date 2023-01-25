from time import sleep
print('='*50)
print(f'{"MENU DE RESTAURANTE":^50}')
print('='*50)

nome_do_bar = str(input('Nome do Estabelecimento: '))
quantidade_itens = int(input('Quantidade de ÍTENS: '))
print('=' * 50)
lista_preço = () ## Tupla
total = 0

cont = 0
for c in range(quantidade_itens):
    cont += 1
    prato = str(input(f'Nome da {cont}° Bebida: '))
    preço = float(input(f'Preço da Bebida R$: '))
    quant = int(input(f'Ítens Consumido(s): '))
    print('=' * 50)
    lista_preço += (prato, preço)

    total = preço * quant

# Contadores e Strings definidas
count = 0
count2 = 1

# Design e detalhes do MENU
estabelecimento = nome_do_bar
print(estabelecimento.center(50,' '))
print('='*50)

# Estrutura que cria o MENU
while True:
    sleep(0.6)
    print(f'{lista_preço[count]:.<40}R$ {lista_preço[count2]:>7.2f}')

    count += 2
    count2 += 2
    if count2 >= len(lista_preço):
        break
print(f"{'VALOR TOTAL:':.<40}R${total:>8.2f}")  ## Não está multiplicando

print('-'*50)
print(f'{"FIM DO PROGRAMA":^50}')
print('='*50)