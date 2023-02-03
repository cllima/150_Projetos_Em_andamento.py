# Crie um programa onde o usuário possa cadastrar 7 valores numericos e cadastre-os em uma
# lista única que mantenha separados os valores PARES e ÍMPARES. NO final mostre os valores
# PARES e ÍMPARES em ordem decrescente.
# Cria-se uma lista com duas dentro, sendo PAR e ÍMPAR.
print('=' * 50)
print(f'{"2 Listas, dentro de 1 lista Principal":^50}'.upper())
print('=' * 50)

lista=[[], []] ## lista [0]PAR e [1]ÍMPAR
valor=0
cont=0
for cont in range(1,8):
    valor=int(input(f'Informe o {cont}º valor: '))
    lista[0].sort()  ## Em ordem crescente PAR
    lista[1].sort()  ## Em ordem crescente ÍMPAR

    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=' * 50)

print(f'Lista completa {lista}')
print(f'Lista com valores PARES: {lista[0]}.\nLista com valores ÍMPARES: {lista[1]}.')
