# Faça um programa que leia nome a peso de várias pessoas, guardando tudo em uma lista. No final Mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
### São 3 lista.
print('=' * 40)
print(f'{"Lista composta e análise de dados":^40}'.upper())
print('=' * 40)
temp=[] ## Lista Temporaria
princ=[] ## Lista principal
maior_p = menor_p = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior_p = menor_p = temp[1]  # maior e menor peso temp[1]
    else:
        if temp[1] > maior_p: # Se o temp[1] é > maior_p
            maior_p = temp[1]
        if temp[1] < menor_p:
            menor_p = temp[1]
    princ.append(temp[:]) ## Cria uma ligação entre princ e temp
    temp.clear()  ## Limpar 0 temp.

    resp=' '
    while resp not in "SN":
        resp=str(input('Continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

print('*'*60)
print(f'Lista: {princ}')
print(f'Foram Cadastrados {len(princ)} pessoas.')

print(f'O MAIOR peso foi de {maior_p}kg. Sendo: ', end='')
for pessoa in princ: ## Varendo a lista princ
    if pessoa[1] == maior_p: # Se o pessoa[1](peso) for igual ao maior_p
        print(f'[{pessoa[0]}] ', end='') # Escreve o nome da pessoa.

print(f'\nO MENOR peso foi de {menor_p}kg. Sendo: ', end='')
for pessoa in princ:
    if pessoa[1] == menor_p:
        print(f'[{pessoa[0]}] ', end='')

